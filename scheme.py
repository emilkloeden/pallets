from typing import List
from rich.console import Console, ConsoleOptions, RenderResult
from rich.segment import Segment, Segments
from rich.style import Style


from color import Color

class ColorScheme:
    def __init__(self, name: str, scheme_type: str, primary: Color, rest: List[Color] = None) -> None:
        self.name = name # needs a fun generator
        self.scheme_type = scheme_type # needs an enum?
        self.primary: Color = primary
        self.rest: List[Color] = [] if rest is None else rest

    def __eq__(self, other):
        return self.colors == other.colors

    @property
    def colors(self):
        return [self.primary] + self.rest

    @colors.setter
    def colors(self, value):
        if not self.primary:
            self.primary = value
        else:
            self.rest.append(value)
        
        print("Set called on ColorScheme#colors")
        print(f"{self.primary=}")
        print(f"{self.rest=}")
        print(f"{self.colors=}")

    @colors.deleter
    def colors(self):
        self.primary = None
        self.rest = []
        print("Delete called on ColorScheme#colors")
        print(f"{self.primary=}")
        print(f"{self.rest=}")
        print(f"{self.colors=}")

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        for color in self.colors:
            text = f"{color.hex_code.upper()}\n"
            yield Segment(text,  Style(bgcolor=f"rgb({color.red},{color.green},{color.blue})"))

