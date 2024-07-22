def tokenize(text: str) -> list[str]:
    return text.upper().split()

print(tokenize("hello world"))  # Output: ['HELLO', 'WORLD']


