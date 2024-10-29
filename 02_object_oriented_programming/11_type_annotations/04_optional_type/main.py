def parse_integer(s: str) -> int | None:
    try:
        return int(s)
    except ValueError:
        return None

def process_number(s: str) -> None:
    number = parse_integer(s)
    if number is not None:
        print(f"The number multiplied by 2 is {number * 2}")
    else:
        print(f"Invalid integer: '{s}'")

if __name__ == "__main__":
    process_number("42")         # Valid integer
    process_number("not a number")  # Invalid integer