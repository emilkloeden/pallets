"""schemegenerator.py

This module exposes `generate_color_scheme` function.

The `generate_color_scheme` function relies on a number
of scheme generator functions defined as private functions
within this module.
"""

import random
from typing import List

from scheme import ColorScheme
from color import Color, generate_random_color
from namegenerator import generate_name

DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME = 4
MIN_NUMBER_OF_COLORS_IN_A_SCHEME = 2
MAX_NUMBER_OF_COLORS_IN_A_SCHEME = 10


def generate_color_scheme(scheme_type: str, primary: Color = None, number_of_colors: int = DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME, renderer=ColorScheme) -> ColorScheme:
    """Generate a color scheme of `scheme_type` providing an optional base 'primary' Color object, a number of colors to define the scheme size, 
    and a renderer class, should you wish to use a different renderer

    Args:
        scheme_type (str): the type of ColorScheme.
        primary (Color, optional): Primary Color. Defaults to None.
        number_of_colors (int, optional): Number of colors in the scheme. Defaults to DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME.
        renderer (_type_, optional): Optional Rendering class. Defaults to ColorScheme.

    Raises:
        ValueError: when the number of of colors requested is outside of the range specified by MIN_NUMBER_OF_COLORS_IN_A_SCHEME and MAX_NUMBER_OF_COLORS_IN_A_SCHEME
        ValueError: when the `scheme_type` value is unrecognised.

    Returns:
        ColorScheme: An instance of a ColorScheme object.
    """    
    if number_of_colors < MIN_NUMBER_OF_COLORS_IN_A_SCHEME or number_of_colors > MAX_NUMBER_OF_COLORS_IN_A_SCHEME:
        raise ValueError(f"Invalid number of colors requested. Supply a number between {MIN_NUMBER_OF_COLORS_IN_A_SCHEME} and {MAX_NUMBER_OF_COLORS_IN_A_SCHEME}")
    
    name = generate_name()
    
    scheme_generator = _scheme_generators.get(scheme_type)
    if not scheme_generator:
        raise ValueError(f"Unrecognised scheme_type '{scheme_type}' supplied.")

    
    colors = scheme_generator(primary=primary, number_of_colors=number_of_colors)
    if not primary:
        primary = colors[0]
        rest = colors[1:]
    else:
        i = colors.index(primary)
        rest = colors[:i] + colors[i+1:]

    return renderer(name=name, scheme_type=scheme_type, primary=primary, rest=rest)

def _generate_monochromatic_theme(primary: Color = None, number_of_colors: int = DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME) -> List[Color]:
    """Return a list of Color objects sharing the same hue. Always includes White and Black.

    Args:
        primary (Color, optional): Primary Color. Defaults to None.
        number_of_colors (int, optional): Number of Color objects to return. Defaults to DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME.

    Returns:
        List[Color]:
    """    
    if not primary:
        primary = generate_random_color()
    
    num_colors_to_generate = number_of_colors - 3 # one each for primary color, white and black
    random_lightness_choices = set([random.random() for _ in range(num_colors_to_generate)])
    
    while len(random_lightness_choices) < num_colors_to_generate:
        random_lightness_choices.add(random.random())
    
    # primary_lightness = primary.lightness
    all_lightness_values = list(random_lightness_choices)
    all_lightness_values.append(0)
    all_lightness_values.append(1)
    # all_lightness_values = sorted(all_lightness_values)
    colors = [
        Color(hue=primary.hue, saturation=primary.saturation, lightness=lightness)
        for lightness
        in all_lightness_values
    ]
    colors.append(primary)
    
    return sorted(colors, key=lambda color: color.hex_code)
    # return ColorScheme(name=name, scheme_type="monochromatic", primary=colors[0], rest=colors[1:])

def _generate_random_color_scheme(primary: Color = None, number_of_colors: int = DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME) -> List[Color]:
    """Return a list of random Color objects. Will include primary Color if supplied

    Args:
        primary (Color, optional): Primary Color. Defaults to None.
        number_of_colors (int, optional): Number of Color objects to return. Defaults to DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME.

    Returns:
        List[Color]:
    """
    length = number_of_colors - 1 if primary else number_of_colors
    
    rest = [
        generate_random_color()
        for _ 
        in range(length)
    ]
    
    if primary:
        return [primary] + rest
    return rest

def _generate_analogous_theme(primary: Color = None, number_of_colors: int = DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME) -> List[Color]:
    """Return a list of Color objects composed of different shades of three hues, separated by 30deg. 

    Args:
        primary (Color, optional): Primary Color. Defaults to None.
        number_of_colors (int, optional): Number of Color objects to return, minimum of three. Defaults to DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME.

    Raises:
        ValueError: when number_of_colors is provided and less than three.

    Returns:
        List[Color]
    """
    if not primary:
        primary = generate_random_color()
    
    if number_of_colors < 3:
        raise ValueError("Analogous schemes must comprise at least three colours.")
    primary_hue = primary.hue
    secondary_hue = (primary.hue + 30) % 360
    tertiary_hue = (primary.hue + 60) % 360
    secondary = Color(hsl=(secondary_hue, primary.saturation, primary.lightness))
    tertiary = Color(hsl=(tertiary_hue, primary.saturation, primary.lightness))

    colors = [primary, secondary, tertiary]
    while len(colors) < number_of_colors:
        colors.append(Color(hue=random.choice([primary_hue, secondary_hue, tertiary_hue]), saturation=random.random(), lightness=random.random()))

    return colors

def _generate_triadic_theme(primary: Color = None, number_of_colors: int = DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME) -> List[Color]:
    """Return a list of Color objects composed of different shades of three equidistant colors. 

    Args:
        primary (Color, optional): Primary Color. Defaults to None.
        number_of_colors (int, optional): Number of Color objects to return, minimum of three. Defaults to DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME.

    Raises:
        ValueError: when number_of_colors is provided and less than three.

    Returns:
        List[Color]
    """    
    if not primary:
        primary = generate_random_color()
    
    if number_of_colors < 3:
        raise ValueError("Triadic schemes must comprise at least three colours.")
    primary_hue = primary.hue
    secondary_hue = (primary.hue + 120) % 360
    tertiary_hue = (primary.hue + 180) % 360
    secondary = Color(hsl=(secondary_hue, primary.saturation, primary.lightness))
    tertiary = Color(hsl=(tertiary_hue, primary.saturation, primary.lightness))

    colors = [primary, secondary, tertiary]
    while len(colors) < number_of_colors:
        colors.append(Color(hue=random.choice([primary_hue, secondary_hue, tertiary_hue]), saturation=random.random(), lightness=random.random()))

    return colors

_scheme_generators = {
    "monochromatic": _generate_monochromatic_theme,
    "analogous": _generate_analogous_theme,
    "triadic": _generate_triadic_theme,
    "random": _generate_random_color_scheme,
}