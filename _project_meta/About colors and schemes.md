# Computers and Representation of Colors

Computers display colors that are represented as a triad of values known as RGB (Red, Green Blue). These are a group of three different values in the range 0-255. In reality these three values are multipled against each other, but it's conceptually simpler to think of them as three separate values. In CSS these are usually converted to hex codes so black in RGB is (0, 0, 0) and in hex is "000000" whilst white is RGB (255, 255, 255) or "FFFFFF". These are commonly prefixed with an octothorpe symbol e.g. '#FFFFFF'

It's worth remembering that Red, Green and Blue is not the same as the three primary colors Red, Yellow and Blue. This results in some translation difficulty when it comes to switching between schemes.

Another means of representing colors is Hue, Saturation, and Lightness (HSL), where Red is represented as (0, 100%, 100%). It is possible to convert between RGB and HSL and back [Al-gore-rhythm](https://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/)

BONUS: Apparently browser dev tools can do the conversion for you if you shift click on a color in the style inspector!

Some RGB, Hex and HSL values:
|Color|Color Type|RGB|Hex|HSL
|--|--|--|--|--|
|Black| |0, 0, 0|#000000|0deg, 0%, 0%|
|White| |255, 255, 255|#FFFFFF|0deg, 0%, 100%|
|Red|Primary|255, 0, 0|#FF0000|0deg, 100%, 50%|
|Lime|Secondary?|0, 255, 0|#00FF00|120deg, 100%, 50%|
|Blue|Primary|0, 0, 255|#0000FF|240deg, 100%, 50%|
|Yellow|Primary|255, 255, 0|#FFFF00|60deg, 100%, 50%|
|Cyan|Secondary?|0, 255, 255|#00FFFF|180deg, 100%, 50%|
|Magenta|Secondary?|255, 0, 255|#FF00FF|300deg, 100%, 50%|
|Silver| |192, 192, 192|#C0C0C0|0deg, 0%, 75%|
|Gray| |128, 128, 128|#808080|0deg, 0%, 50%|
|Maroon| |128, 0, 0|#800000|0deg, 100%, 25%|
|Olive| |128, 128, 0|#808000|60deg, 100%, 25%|
|Green| |0, 128, 0|#008000|120deg, 100%, 25%|
|Purple| |128, 0, 128|#800080|300deg, 100%, 25%|
|Teal| |0, 128, 128|#008080|180deg, 100%, 25%|
|Navy| |0, 0, 128|#000080|240deg, 100%, 25%|

# Colors

## Hue

    Hue refers to the pure pigment of a color, without tint or shade. In that respect, hue can be interpreted as the origin of a color. Any one of the six primary and secondary colors is a hue.

Source: [Introduction to the color wheel](https://careerfoundry.com/en/blog/ui-design/introduction-to-color-theory-and-color-palettes/#introduction-to-the-color-wheel)

## Shade

    Shade refers to how much black is added into the hue. As such, shade darkens a color.

Source: [Introduction to the color wheel](https://careerfoundry.com/en/blog/ui-design/introduction-to-color-theory-and-color-palettes/#introduction-to-the-color-wheel)

To add shade you should multiple each component by a fraction of its value (e.g. 1/4, 1/2 etc.)
Thus if we start with yellow (255, 255, 0) (#FFFF00) and we multiply the R, G, and B, values by 0.25 we get (63, 63, 0) (after rounding) which is a darker shade of yellow than if we were to multiply the values by 0.8 (203, 203, 0).

Another means of representing colors is Hue, Saturation, and Lightness (HSL), where Red is represented as (0, 100%, 100%). Adding shade here is done by reducing the lightness level alone. RGB(255, 0, 0) translates to HSL(0, 100%, 50%) and as such to add a little `shade` we could go with HSL(0, 100%, 40%) or to add `tint` HSL(0, 100%, 60%).

Here's a quick and dirty script to paste into a browser console that demonstrates this (it overwrites the content of your page, so exercise caution):

```js
function hslMe(n = 6, hue = 0) {
  document.body.innerHTML = `<div><ul id="ul">${"<li>COLORS, OH MY!</li>".repeat(
    n
  )}</ul></div>`;
  const li = Array.from(document.querySelectorAll("li"));
  li.forEach((el, i) => {
    el.setAttribute(
      "style",
      `font-size:6rem; color: hsl(${hue}, 100%, ${
        100 * (1 - (1 / (li.length - 1)) * i)
      }%`
    );
  });
}
// 6 equidistant values (5 steps) of White -> Red -> Black
hslMe();

// 4 equidistant values (3 steps) of White -> Yellow -> Black
hslMe(4, 60);
```

## Tint

    The opposite of shade, tint refers to how much white is added to a color. As such, tint lightens a color.

Source: [Introduction to the color wheel](https://careerfoundry.com/en/blog/ui-design/introduction-to-color-theory-and-color-palettes/#introduction-to-the-color-wheel)

So, if we can manipulate hsl values we can do this by increasing the lightness level

## Tone

    Tone is the result of a color that has had both white and black added to it. In other words, tone refers to any hue that has been modified with the addition of grey—as long as the grey is purely neutral (only containing white and black).

Source: [Introduction to the color wheel](https://careerfoundry.com/en/blog/ui-design/introduction-to-color-theory-and-color-palettes/#introduction-to-the-color-wheel)

While one [resource](https://www.smashingmagazine.com/2010/02/color-theory-for-designers-part-2-understanding-concepts-and-terminology/) suggests tone is different to saturation, 0% saturation is grey and 100% represents the absence of grey, so I'd suggest the S in HSL would work should a scheme require the addition of tone.

# Schemes

## Monochromatic

    Monochromatic color schemes are formed using various tones and shades of one single color.

Source: [What are the different type of color palletes](https://careerfoundry.com/en/blog/ui-design/introduction-to-color-theory-and-color-palettes/#what-are-the-different-type-of-color-palettes)

Key words there being: `tone`, `shade` and `color` (or hue, really).

Thus if HSL is available we can generate a collection of values with a different lighness level to achieve this theme.
