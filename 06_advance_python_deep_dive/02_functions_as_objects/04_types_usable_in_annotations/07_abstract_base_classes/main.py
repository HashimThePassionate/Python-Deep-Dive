from collections.abc import Mapping

def name2hex(name: str, color_map: Mapping[str, int]) -> str:
    hex_value = color_map.get(name)
    if hex_value is None:
        raise ValueError(f"Name '{name}' not found in color_map.")
    return f"#{hex_value:06x}"


color_map = {
    'red': 0xff0000,
    'green': 0x00ff00,
    'blue': 0x0000ff
}

print(name2hex('red', color_map))  # Output: #ff0000