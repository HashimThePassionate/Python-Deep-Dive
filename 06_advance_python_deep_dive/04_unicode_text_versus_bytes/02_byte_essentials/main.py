cafe = bytes('café', encoding='utf_8')
print(cafe)  # Output: b'caf\xc3\xa9'

print(cafe[0])  # Output: 99

print(cafe[:1])  # Output: b'c'
print(cafe[:2])  # Output: b'ca'

cafe_arr = bytearray(cafe)
print(cafe_arr)  # Output: bytearray(b'caf\xc3\xa9')
print(cafe_arr[-1:])  # Output: bytearray(b'\xa9')
print(cafe_arr[::-1])  # Output: bytearray((b'\xa9\xc3fac')
