from rich.console import Console, ConsoleOptions, RenderResult
from rich.segment import Segment, Segments
from rich.style import Style

from scheme import ColorScheme


class ColorSchemeConsole(ColorScheme):
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        colors = sorted(self.colors, key=lambda x: x.hex_code, reverse=True)

        for color in colors:
            text = f"{color.hex_code.upper()}\n"
            yield Segment(text,  Style(bgcolor=f"rgb({color.red},{color.green},{color.blue})"))
