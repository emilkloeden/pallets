import random
from typing import List

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
    
    return sorted(colors, key=lambda color: color.hex_code)
    # return ColorScheme(name=name, scheme_type="monochromatic", primary=colors[0], rest=colors[1:])

def _generate_random_color_scheme(primary: Color = None, number_of_colors: int = DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME) -> List[Color]:
    length = number_of_colors - 1 if primary else number_of_colors
    
    rest = [
        generate_random_color()
        for _ 
        in range(length)
    ]
    
    if primary:
        return [primary] + rest
    return rest


_scheme_generators = {
    "monochromatic": _generate_monochromatic_theme,
    "random": _generate_random_color_scheme,
}