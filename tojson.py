import json
import random

from color import Color
from scheme import ColorScheme
from schemegenerator import generate_color_scheme


def encode(z):
    if isinstance(z, Color):
        return {
        "__obj_type": "Color",
            "hex_code": z.hex_code
        }
    elif isinstance(z, ColorScheme):
        return {
            "__obj_type": "ColorScheme",
            "name": z.name,
            "scheme_type": z.scheme_type,
            "primary": z.primary,
            "rest": z.rest
        }
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

def decode(dict_):
    if "__obj_type" in dict_:
        obj_type = dict_["__obj_type"]
        if obj_type == "Color":
            return Color(hex_code=dict_["hex_code"])
        elif obj_type == "ColorScheme":
            name = dict_["name"]
            scheme_type = dict_["scheme_type"]
            primary = dict_["primary"]
            rest = dict_["rest"]
            return ColorScheme(name=name, scheme_type=scheme_type, primary=primary, rest=rest)


def short_hand_for_web_one_way_encoding(z):
    if isinstance(z, Color):
        return z.hex_code
    elif isinstance(z, ColorScheme):
        return {
            "name": z.name,
            "scheme_type": z.scheme_type,
            "colors": z.colors
        }
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")



schemes = [
    generate_color_scheme(scheme_type="random", primary=None, number_of_colors=random.randint(3, 9))
    for _
    in range(50)
]

scheme = schemes[0]
j = json.dumps(scheme, default=encode)
s = json.loads(j, object_hook=decode)


with open("someschemes.json", "w") as f:
    json.dump(schemes, f, default=encode, indent=2)

with open("someschemesforweb.json", "w") as f:
    json.dump(schemes, f, default=short_hand_for_web_one_way_encoding, indent=2)