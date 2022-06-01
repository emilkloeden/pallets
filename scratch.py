"""Messing around with the output part
"""

from time import sleep
from rich.console import Console
# We want to print all the colours!
console = Console(color_system="truecolor")

def _is_in_valid_range(value: int, min_: int, max_: int) -> bool:
    return min_ <= value <= max_

def _is_in_valid_range_for_rgb(value: int) -> bool:
    return _is_in_valid_range(value, 0, 255)

def print_rgb(red, green, blue, length=10, fg_color="default") -> None:
    
    if all([_is_in_valid_range_for_rgb(value) for value in [red, green, blue]]):
        bg_color = f"rgb({red},{green},{blue})"
        fg_text = f"rgb({red:3d},{green:3d},{blue:3d})"
        console.print(fg_text, style=f"{fg_color} on {bg_color}")
    else:
        raise ValueError("Invalid RGB value supplied. All arguments must be in the range 0-255 inclusive.")

step_size = 10
for red in range(0, 255, step_size):
    for green in range(0, 255, step_size):
        for blue  in range(0, 255, step_size):
            print_rgb(red, green, blue)
            # sleep(0.01)