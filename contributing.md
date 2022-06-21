# Contributing

Contributions are welcome, but we're realistic and don't expect any.

## What to contribute

Possibly the easiest way to contribute would be to add a scheme generator function (see: `schemegenerator.py`). Refer also `TODO.md` and `PLAN.md` for contribution ideas and a vague roadmap.

## How to contribute

1. Create an issue indicating the desired feature/fix you wish to implement
1. Fork the repository
1. Make your changes locally
1. Create a pull request

## How to write a scheme generator function

Add a private function definition to `schemegenerator.py`. function name should take the format `_generate_{scheme_name}_theme` and take a subset of the the keyword arguments `name: str, primary: Color = None, number_of_colors: int = DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME):`

For example:

```py
def _generate_poor_mans_xmas_example_theme(primary: Color = None, number_of_colors: int = DEFAULT_NUMBER_OF_COLORS_IN_A_SCHEME) -> List[Color]:
    return [Color(css="red"), Color(css="green")]
```

- As an aside: there is a minumum of two and a maximum of ten colors configured in `schemegenerator.py` however currently these are enforced only on user input to the parent `generate_color_scheme` function and a scheme generator is welcome to generate schemes as big or small as it wishes.

Then add an entry to the `_scheme_generators` dictionary e.g.

```py
_scheme_generators = {
    "monochromatic": _generate_monochromatic_theme,
    "random": _generate_random_color_scheme,
    "poor_mans_xmas_example_theme": _generate_poor_mans_xmas_example_theme,

}

```
