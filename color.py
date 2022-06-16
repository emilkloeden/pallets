import random

class Color:
    def __init__(self, *, hex_code=None, rgb=None, red=None, green=None, blue=None, hsl=None, hue=None, saturation=None, lightness=None) -> None:
        if hex_code:
            self.hex_code = self.normalise_hex_code(hex_code)
            self.hex_2_rgb()
            self.rgb_2_hsl()
            
        elif rgb:
            self.rgb = rgb
            self.red, self.green, self.blue = rgb
            self.rgb_2_hex()
            self.rgb_2_hsl()
        elif _all_red_green_blue_supplied_and_valid(red, green, blue):
            self.red = red
            self.green = green
            self.blue = blue
            self.rgb = (self.red, self.green, self.blue)
            self.rgb_2_hex()
            self.rgb_2_hsl()
        elif hsl:
            self.hsl = hsl
            self.hue, self.saturation, self.lightness = self.hsl
            self.hsl_2_rgb()
            self.rgb_2_hex()
        elif 0 <= hue <= 360 and 0 <= saturation <= 1 and 0 <= lightness <= 1:
            self.hue = hue
            self.saturation = saturation
            self.lightness = lightness
            self.hsl = (self.hue, self.saturation, self.lightness)
            self.hsl_2_rgb()
            self.rgb_2_hex()
        else:
            raise TypeError(f"Unable to initialise Color object with arguments: ")

    def __repr__(self):
        rgb = f"rgb({self.red},{self.green},{self.blue})"
        hsl = f"hsl({self.hue},{self.saturation*100:.1f}%,{self.lightness*100:.1f}%)"
        return f"{self.__class__.__name__}({self.hex_code}, {rgb}, {hsl})"
    
    def normalise_hex_code(self, hex_code):
        return hex_code if hex_code[0] == "#" else f"#{hex_code}"

    def hex_2_rgb(self):
        self.red = int(self.hex_code[1:3], 16)
        self.green = int(self.hex_code[3:5], 16)
        self.blue = int(self.hex_code[5:7], 16)
        self.rgb = (self.red, self.green, self.blue)

    def rgb_2_hex(self):
        red, green, blue = self.rgb
        hex_code  = "#"
        for i in [red, green, blue]:
            hex_code += f"{i:0>2x}"
        self.hex_code = hex_code

    def rgb_2_hsl(self):
        normalised_red = self.red / 255
        normalised_green = self.green / 255
        normalised_blue = self.blue / 255
        
        max_normalised = max(normalised_red, normalised_green, normalised_blue)
        min_normalised = min(normalised_red, normalised_green, normalised_blue)
        
        delta = max_normalised - min_normalised
        
        if delta == 0:
            hue = 0
        elif max_normalised == normalised_red:
            hue = ((normalised_green - normalised_blue) / delta ) % 6
        elif max_normalised == normalised_green:
            hue = (normalised_blue - normalised_red) / delta + 2
        else:
            hue = (normalised_red - normalised_green) / delta + 4

        hue = round(hue * 60)

        if hue < 0:
            hue += 360

        lightness = round((max_normalised + min_normalised) / 2, 2)
        saturation = 0 if delta == 0 else round(delta / (1 - abs(2 * lightness - 1)), 2)

        self.hue = hue
        self.saturation = saturation
        self.lightness = lightness
        self.hsl = (self.hue, self.saturation, self.lightness)

    def hsl_2_rgb(self):
        hue = self.hue
        saturation = self.saturation
        lightness = self.lightness

        c = (1 - abs(2 * lightness - 1)) * saturation
        x = c * (1 - abs((hue / 60) % 2 - 1))
        m = lightness - c / 2

        if 0 <= hue < 60:
            red = c
            green = x
            blue = 0
        elif 60 <= hue < 120:
            red = x
            green = c
            blue = 0
        elif 120 <= hue < 180:
            red = 0
            green = c
            blue = x
        elif 180 <= hue < 240:
            red = 0
            green = x
            blue = c
        elif 240 <= hue < 300:
            red = x
            green = 0
            blue = c
        elif 300 <= hue < 360:
            red = c
            green = 0
            blue = x

        red = round((red + m) * 255)
        green = round((green + m) * 255)
        blue = round((blue + m) * 255)

        self.red = red
        self.green = green
        self.blue = blue
        self.rgb = (self.red, self.green, self.blue)
            

def _all_red_green_blue_supplied_and_valid(red, green, blue) -> bool :
    return (
        red is not None 
        and green is not None 
        and blue is not None 
        and 0 <= red <= 255 
        and 0 <= green <= 255 
        and 0 <= blue <= 255
    )

def generate_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return Color(red=red, green=green, blue=blue)