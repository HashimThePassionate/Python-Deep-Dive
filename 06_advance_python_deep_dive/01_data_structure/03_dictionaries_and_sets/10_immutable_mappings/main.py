from types import MappingProxyType

# Creating a dictionary
d = {1: 'A'}

# Creating a read-only mappingproxy instance from the dictionary
d_proxy = MappingProxyType(d)

# Accessing items in the proxy
print(d_proxy)  # Output: mappingproxy({1: 'A'})
print(d_proxy[1])  # Output: 'A'

# Attempting to modify the proxy (this will raise an error)
# try:
#     d_proxy[2] = 'x'
# except TypeError as e:
#     print(e)  # Output: 'mappingproxy' object does not support item assignment

# Modifying the original dictionary
d[2] = 'B'

# Changes in the original dictionary are reflected in the proxy
print(d_proxy)  # Output: mappingproxy({1: 'A', 2: 'B'})
print(d_proxy[2])  # Output: 'B'


class Board:
    def __init__(self):
        self._pins = {1: 'Pin1', 2: 'Pin2'}  # Private mapping
        self.pins = MappingProxyType(self._pins)  # Public read-only proxy


# Example usage
board = Board()
print(board.pins[1])  # Output: 'Pin1'

# Attempting to modify the proxy (this will raise an error)
# try:
#     board.pins[3] = 'Pin3'
# except TypeError as e:
#     print(e)  # Output: 'mappingproxy' object does not support item assignment

# Modifying the private mapping
board._pins[3] = 'Pin3'
print(board.pins[3])  # Output: 'Pin3'
