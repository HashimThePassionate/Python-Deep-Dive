from typing import Annotated

class StringLength:
    def __init__(self, min_len: int, max_len: int):
        self.min_len = min_len
        self.max_len = max_len

username: Annotated[str, StringLength(5, 15)] = "Hi"  # Invalid, too short

def validate_annotated(var, metadata) -> None:
    if isinstance(metadata, StringLength):
        if not (metadata.min_len <= len(var) <= metadata.max_len):
            raise ValueError(f"Length of '{var}' is not between {metadata.min_len} and {metadata.max_len}.")

# Validation
try:
    validate_annotated(username, StringLength(5, 15))
    print(f"'{username}' is valid!")
except ValueError as e:
    print(e)
