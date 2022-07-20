"""pallets.py

This module provides a CLI to request the generation of color schemes.
"""
import argparse
import random

from typing import List
from argparse import ArgumentParser

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

from .color import Color
from .scheme import ColorScheme
from .schemegenerator import scheme_types as SCHEME_TYPES, generate_color_scheme
from .consoleschemerenderer import ColorSchemeConsole


def parse_arguments() -> argparse.Namespace:
    parser = ArgumentParser()
    parser.add_argument("scheme_type", choices=SCHEME_TYPES, default=None, nargs="?")
    parser.add_argument("-n", "--number", type=int, default=5, help="Number of colors in a scheme. Defaults to 5.")
    parser.add_argument("-p", "--primary", type=str, help="Primary color. Hex value or css color name to use as a base for the scheme.")
    parser.add_argument("-m", "--max", type=int, default=5, help="maximum number of color schemes to print. Defaults to 5.")

    return parser.parse_args()


def generate_schemes(args: argparse.Namespace) -> List[ColorScheme]:
    try:
        if args.primary:
            try:
                primary = _get_color_from_string(args.primary)
            except ValueError:
                print(f"'{args.primary}' could not be converted to a color.")
                exit()
        else:
            primary = None
        
        return [
            generate_color_scheme(scheme_type=_choose_scheme_type(args.scheme_type), primary=primary, number_of_colors=args.number, renderer=ColorSchemeConsole)
            for _ 
            in range(args.max)
        ]
    except Exception as e:
        print(e)
        exit()

def _choose_scheme_type(scheme_type: str or None):
    """Returns a function call to randomly select from `scheme_type` if `scheme_type` is 'any'
    otherwise it just returns `scheme_type`

    Args:
        scheme_type (str) or None: one of the values of `SCHEME_TYPES` or 'any'

    Returns:
        str or random.choice(SCHEME_TYPES)
    """    
    if scheme_type:
        return scheme_type
    return random.choice(SCHEME_TYPES)


def _get_color_from_string(color_string: str) -> Color:
    """Return Color object by first attempting to parse `color_string` as a css color name, then as a hex value.

    Args:
        color_string (str): css color name or hex value

    Returns:
        Color:
    """    
    try:
        return Color(css=color_string)
    except ValueError:
        return _get_color_by_hex_code(color_string)


def _get_color_by_hex_code(color_string: str) -> Color:
    return Color(hex_code=color_string)


def print_schemes(schemes: List[ColorScheme]) -> None:
    console = Console()

    max_scheme_name_length = max([len(scheme.name) for scheme in schemes]) + 4
    panels = [
        Panel(
            scheme,
            title=scheme.name, 
            subtitle=f"({scheme.scheme_type})", 
            width=max_scheme_name_length,
        )
        for scheme 
        in schemes
        ]

    console.print(Columns(panels))


def main() -> None:
    args = parse_arguments()
    schemes = generate_schemes(args)
    print_schemes(schemes)


if __name__ == "__main__":
    main()