# Description

This application will generate a range of color palletes using optional filters:

- Number of colours (there should be a maximum limit - what is it?)
- Color pallet type (one of):
  -- Monochromatic
  -- Analogous
  -- Complementary
  -- Split-complementary
  -- Triadic
  -- Tetradic
- Color (name or hex representation), number of supplied arguments cannot exceed that which a color pallet ruling would define (e.g. not two if 'Monochromatic' is chosen). Supplying blue and green should only return a pallet that contains both these colors, not either of those.
  -- \*This is potentially tricky and may want to be rethought as choosing two colors may be valid, but the combination of those two might not be valid for that theme.

# Technical Note

This should be broken up into three parts (or modules):

1. Receiving input from the user
2. Generating pallets
3. Displaying pallets

Splitting the code into these three parts, would allow swapping out means of getting input and display, whilst keeping the pallet generation logic consistent.

# Implementation thoughts

1. We should use one function per color pallet type.
2. We should start with the generating pallets module and the Monochromatic type
3. For an initial implementation I would like to develop a command-line based app, hence using argparse for the user input module is a good fit
4. For an initial implementation of the display I would like to see output on the command line, I'm not sure yet how this would be best done.

# References

- [Career Foundry - Introduction to Color Theory and Color Palletes](https://careerfoundry.com/en/blog/ui-design/introduction-to-color-theory-and-color-palettes/#:~:text=Color%20theory%20is%20a%20framework,aesthetic%20and%20a%20psychological%20level.)
- [The Color API - Scheme Reference](https://www.thecolorapi.com/docs#schemes-generate-scheme-get)
