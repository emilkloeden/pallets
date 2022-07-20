# TODO

## "Front part"

- [ ] Terminal layer to allow user to control output (e.g. of `columnpanelui.py`). `argparse` should be used for this.

## "Middle part"

### Color scheme functions

- [ ] Monochromatic color scheme generator function with precise steps between levels (current version uses random values)
- [ ] Analogous color scheme generator function with a little more precision when > 3 values chosen (current version uses precise hue and random saturation and lightness values for a random choice of the first three values)
- [ ] An Analogous colour scheme generator function that allows for random steps in hues between primary, secondary and tertiary colours (current version increments by exactly 30deg).
- [ ] Complementary color scheme generator function
- [ ] Split-complementary color scheme generator function
- [ ] Tetradic color scheme generator function

### Other

- [ ] Database persistence? When do we want to generate schemes and when do we want to just view previously generated themes?

### General

- [ ] Documentation! Especially Docstrings (https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html). At present there aren't any :/
- [ ] Clean up files in repo
- [ ] Separate applications for scheme generation and filtering/viewing?
- [ ] Add Black formatting git hook on pre-commit, push?
- [ ] Tag a release on GitHub
- [ ] Fix Firefox warning about SVG using calc() in width, height. See (https://css-tricks.com/scale-svg/).
- [ ] Update splash page to add PyPI repo link
- [ ] Automate versioning
- [ ] Automate PyPI deployment (GitHub Actions?)

## "Back part"

- [ ] JSON API application
- [ ] Web frontend application
- [ ] Web components to power web frontend application

# DONE

- [x] Base classes (Color, ColorScheme)
- [x] Scheme generator functionality skeleton
- [x] Monochromatic color scheme generator function
- [x] Random color scheme generator function
- [x] Analogous color scheme generator function
- [x] Triadic color scheme generator function
- [x] Some form of UI to view color schemes in the terminal - see `columnpanelui.py`
- [x] Pull `rich`-specific code out of ColorScheme class
- [x] Get package onto PyPI?
