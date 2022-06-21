import random

from scheme import ColorScheme
from color import Color, generate_random_color
from namegenerator import generate_name

DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME = 4
MIN_NUMBER_OF_COLORS_IN_A_SCHEME = 2
MAX_NUMBER_OF_COLORS_IN_A_SCHEME = 10





def generate_color_scheme(scheme_type: str, primary: Color = None, number_of_colors: int = DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME, renderer=ColorScheme) -> ColorScheme:
    if number_of_colors < MIN_NUMBER_OF_COLORS_IN_A_SCHEME or number_of_colors > MAX_NUMBER_OF_COLORS_IN_A_SCHEME:
        raise ValueError(f"Invalid number of colors requested. Supply a number between {MIN_NUMBER_OF_COLORS_IN_A_SCHEME} and {MAX_NUMBER_OF_COLORS_IN_A_SCHEME}")
    
    name = generate_name()
    
    if scheme_type == "monochromatic":
        colors = _generate_monochromatic_theme(name, primary, number_of_colors)
    elif scheme_type == "random":
        colors = _generate_random_color_scheme(name, number_of_colors)
    else:
        raise ValueError(f"Unrecognised scheme_type '{scheme_type}' supplied.")

    return renderer(name=name, scheme_type=scheme_type, primary=colors[0], rest=colors[1:])

def _generate_monochromatic_theme(name: str, primary: Color = None, number_of_colors: int = DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME):
    # Work out if I should do rounding here or not
    if not primary:
        primary = generate_random_color()
    
    num_colors_to_generate = number_of_colors - 3 # one each for primary color, white and black
    random_lightness_choices = set([random.random() for _ in range(num_colors_to_generate)])
    
    while len(random_lightness_choices) < num_colors_to_generate:
        random_lightness_choices.add(random.random())
    
    primary_lightness = primary.lightness
    all_lightness_values = list(random_lightness_choices)
    all_lightness_values.append(primary_lightness)
    all_lightness_values.append(0)
    all_lightness_values.append(1)
    all_lightness_values = sorted(all_lightness_values)
    colors = [
        Color(hue=primary.hue, saturation=primary.saturation, lightness=lightness)
        for lightness
        in all_lightness_values
    ]
    
    return colors
    # return ColorScheme(name=name, scheme_type="monochromatic", primary=colors[0], rest=colors[1:])

def _generate_random_color_scheme(name: str, number_of_colors: int = DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME):
    colors = [
        generate_random_color()
        for _ 
        in range(number_of_colors)
    ]

    return colors
    # return ColorScheme(name=name, scheme_type="random", primary=colors[0], rest=colors[1:])
