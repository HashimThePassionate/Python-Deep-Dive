label = "Hello"
print(label.isalpha())  # Output: True

text = "Hello, World!"
print(text.isprintable())  # Output: True

number = "12345"
print(number.isdecimal())  # Output: True

numeric_string = "12345"
print(numeric_string.isnumeric())  # Output: True

fraction_string = "⅔"
print(fraction_string.isnumeric())  # Output: True

text = "Hello"
folded_text = text.casefold()
print(folded_text)  # Output: "hello"