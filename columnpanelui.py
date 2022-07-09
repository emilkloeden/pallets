import random

from rich.align import Align
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from consoleschemerenderer import ColorSchemeConsole

from schemegenerator import generate_color_scheme
from color import Color, RED, GREEN, BLUE

primary_colors = [RED, GREEN, BLUE]

nicer_colors = [
    Color(css="cornflowerblue"),
    Color(css="darkslategray"),
    Color(css="maroon")
]

schemes = [
    generate_color_scheme(scheme_type="random", primary=random.choice(nicer_colors), number_of_colors=random.randint(7, 7), renderer=ColorSchemeConsole)
    for _
    in range(20)
]
monochrome_schemes = [
    generate_color_scheme(scheme_type="monochromatic", primary=RED, number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="monochromatic", primary=GREEN, number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="monochromatic", primary=BLUE, number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="monochromatic", primary=Color(css="aquamarine"), number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="monochromatic", primary=Color(css="lightseagreen"), number_of_colors=8, renderer=ColorSchemeConsole),
    
]

analogous_schemes = [
    generate_color_scheme(scheme_type="analogous", primary=RED, number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="analogous", primary=GREEN, number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="analogous", primary=BLUE, number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="analogous", primary=Color(css="aquamarine"), number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="analogous", primary=Color(css="lightseagreen"), number_of_colors=8, renderer=ColorSchemeConsole),
]

triadic_schemes = [
    generate_color_scheme(scheme_type="triadic", primary=RED, number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="triadic", primary=GREEN, number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="triadic", primary=BLUE, number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="triadic", primary=Color(css="aquamarine"), number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="triadic", primary=Color(css="lightseagreen"), number_of_colors=8, renderer=ColorSchemeConsole),
]

schemes = analogous_schemes + triadic_schemes

# schemes += monochrome_schemes
console = Console()


scheme = schemes[-1]
max_scheme_name_length = max([len(scheme.name) for scheme in schemes]) + 4
panels = [
    Panel(
        # Align.center(scheme, pad=True), # Using this stops the background stretching across the width of the panel 
        scheme,
        title=scheme.name, 
        subtitle=f"({scheme.scheme_type})", 
        width=max_scheme_name_length,
    )
    for scheme 
    in schemes
    ]

console.print(Columns(panels))

