from typing import List
from color import Color

class ColorScheme:
    def __init__(self, name: str, scheme_type: str, primary: Color, rest: List[Color] = None) -> None:
        self.name = name # needs a fun generator
        self.scheme_type = scheme_type # needs an enum?
        self.primary: Color = primary
        self.rest: List[Color] = [] if rest is None else rest 

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



#######TODO
"""Determine an export to JSON function, returning something like: 
{
    "name": "Blah",
    "scheme_type": "random",
    "primary": "#FF0022",
    "rest": [
        "#33CC33",
        "#22AABB",
    ]

}

then we'd need a decoder as well.
"""