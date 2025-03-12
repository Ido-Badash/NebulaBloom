from kivy.core.clipboard import Clipboard

def rgba_to_kivy(r: int, g: int, b: int, a: int = 255,
                ndigits: int = 3, copy_to_keyboard: bool = True):
    """Converts the normal rgba format to Kivy rgba format."""
    rgba = tuple(round(x / 255, ndigits) for x in (r, g, b, a))
    if copy_to_keyboard:
        rgba_string = ", ".join(map(str, rgba))
        Clipboard.copy(rgba_string)
    return rgba

if __name__ == "__main__":
    my_rgba = (230, 255, 0, 120)
    kivy_color = rgba_to_kivy(*my_rgba)