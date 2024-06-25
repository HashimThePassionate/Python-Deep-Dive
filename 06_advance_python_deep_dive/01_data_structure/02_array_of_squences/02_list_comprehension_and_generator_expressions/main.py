symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)  # Output: [36, 162, 163, 165, 8364, 164]

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)  # Output: [36, 162, 163, 165, 8364, 164]


# List comprehension
x = 'ABC'
codes = [ord(x) for x in x]
print(x)    # Output: 'ABC'
print(codes)  # Output: [65, 66, 67]
# print(c)

# List comprehension with walrus operator
x = 'ABC'
codes = [last := ord(c) for c in x]
print(last)   # Output: 67


symbols = '$¢£¥€¤'
b = [ord(s) for s in symbols]
print(b)
# output: [36, 162, 163, 165, 8364, 164]


symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 163]
print(beyond_ascii)
# Output: [165, 8364, 164]

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)


symbols = '$¢£¥€¤'
tuple_genexp = tuple(ord(symbol) for symbol in symbols)
print(tuple_genexp)
# Output: (36, 162, 163, 165, 8364, 164)

import array
array_genexp = array.array('I', (ord(symbol) for symbol in symbols))
print(array_genexp)
# Output: array('I', [36, 162, 163, 165, 8364, 164])