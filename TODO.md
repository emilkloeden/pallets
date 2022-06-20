# TODO

## "Front part"

- [ ] Terminal layer to allow user to control output (e.g. of `columnpanelui.py`). `argparse` should be used for this.

## "Middle part"

### Color scheme functions

- [ ] Monochromatic color scheme generator function with precise steps between levels (current version uses random values)
- [ ] Analogous color scheme generator function
- [ ] Complementary color scheme generator function
- [ ] Split-complementary color scheme generator function
- [ ] Triadic color scheme generator function
- [ ] Tetradic color scheme generator function

### Other

- [ ] Pull `rich`-specific code out of ColorScheme class
- [ ] Database persistence? When do we want to generate schemes and when do we want to just view previously generated themes?

### General

- [ ] Clean up files in repo
- [ ] Get package onto PyPI?
- [ ] Separate applications for scheme generation and filtering/viewing?

## "Back part"

- [ ] JSON API application
- [ ] Web frontend application
- [ ] Web components to power web frontend application

# DONE

- [x] Base classes (Color, ColorScheme)
- [x] Scheme generator functionality skeleton
- [x] Monochromatic color scheme generator function
- [x] Random color scheme generator function
- [x] Some form of UI to view color schemes in the terminal - see `columnpanelui.py`
