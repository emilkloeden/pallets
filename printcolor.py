import random
from rich.console import Console

from color import Color
from scheme import ColorScheme
from schemegenerator import generate_color_scheme

CONSOLE_WIDTH = 30
# We want to print all the colours!
console = Console(color_system="truecolor", width=CONSOLE_WIDTH)

PREFERRED_FORMAT = "rgb" # values: 'hex_code', 'rgb' or 'hsl'
preferred_formats = ["hex_code", "rgb", "hsl"]

def _print_hex_code(color):
    bg_color = f"rgb({color.red},{color.green},{color.blue})"
    console.print(color.hex_code, style=f"default on {bg_color}", justify="center")


def _print_rgb(color):
    fg_text = f" rgb({color.red:3d},{color.green:3d},{color.blue:3d}) "
    bg_color = f"rgb({color.red},{color.green},{color.blue})"
    console.print(fg_text, style=f"default on {bg_color}", justify="center")

def _print_hsl(color):
    fg_text = f"hsl({color.hue:3d}, {color.saturation*100:5.1f}%, {color.lightness*100:5.1f}%)"
    bg_color = f"rgb({color.red},{color.green},{color.blue})"
    console.print(fg_text, style=f"default on {bg_color}", justify="center")


if PREFERRED_FORMAT == "hex_code":
    print_color = _print_hex_code
elif PREFERRED_FORMAT == "rgb":
    print_color = _print_rgb
elif PREFERRED_FORMAT == "hsl":
    print_color = _print_hsl

else:
    raise ValueError(f"No or invalid value provided as preferred format for printing. Options are {', '.join(preferred_formats)}")



def print_color_scheme(scheme: ColorScheme):
    console.print(scheme.name, justify="center")
    console.print(f"Scheme Type: {scheme.scheme_type} ({len(scheme.colors)} colors)")
    console.print(f"Primary color: rgb({scheme.primary.rgb})")
    for color in scheme.colors:
        print_color(color)
    print()








RED_RGB = (255, 0, 0)
COLOR_RED = Color(rgb=RED_RGB)
monochromatic_random_six_red = generate_color_scheme(scheme_type="monochromatic", primary=COLOR_RED, number_of_colors=6)
print_color_scheme(monochromatic_random_six_red)
random_color_scheme_3 = generate_color_scheme(scheme_type="random", number_of_colors=3)
print_color_scheme(random_color_scheme_3)
random_color_scheme_10 = generate_color_scheme(scheme_type="random", number_of_colors=10)
print_color_scheme(random_color_scheme_10)