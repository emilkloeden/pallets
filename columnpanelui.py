import random

from rich.align import Align
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from consoleschemerenderer import ColorSchemeConsole

from schemegenerator import generate_color_scheme
from color import RED, GREEN, BLUE

primary_colors = [RED, GREEN, BLUE]

schemes = [
    generate_color_scheme(scheme_type="random", primary=random.choice(primary_colors), number_of_colors=random.randint(3, 9), renderer=ColorSchemeConsole)
    for _
    in range(10)
]
monochrome_schemes = [
    generate_color_scheme(scheme_type="monochromatic", primary=RED, number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="monochromatic", primary=GREEN, number_of_colors=8, renderer=ColorSchemeConsole),
    generate_color_scheme(scheme_type="monochromatic", primary=BLUE, number_of_colors=8, renderer=ColorSchemeConsole),
]

schemes += monochrome_schemes
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
