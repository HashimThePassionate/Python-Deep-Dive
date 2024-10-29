from ctypes import string_at
from sys import getsizeof
from binascii import hexlify

a = 0b01010000_01000001_01010100  # Binary number
print(a)  # Output: 5259604

text = "PAT"
print(string_at(id(text), getsizeof(text)))
print(hexlify(string_at(id(text), getsizeof(text))))
