# Immutable Mappings

The mapping types provided by the standard library are all mutable, but there are scenarios where preventing changes to a mapping is necessary. For instance, in hardware programming libraries like Pingo, the `board.pins` mapping represents the physical GPIO pins on the device. Since the hardware cannot be changed via software, any modification to the mapping would make it inconsistent with the physical reality of the device.

To address this, Python's `types` module provides a wrapper class called `MappingProxyType`. This class, given a mapping, returns a `mappingproxy` instance that is a read-only but dynamic proxy for the original mapping. This means that updates to the original mapping can be seen in the `mappingproxy`, but changes cannot be made through it.

## Example of `MappingProxyType`

Here is a brief demonstration of how `MappingProxyType` works:

```python
from types import MappingProxyType

# Creating a dictionary
d = {1: 'A'}

# Creating a read-only mappingproxy instance from the dictionary
d_proxy = MappingProxyType(d)

# Accessing items in the proxy
print(d_proxy)  # Output: mappingproxy({1: 'A'})
print(d_proxy[1])  # Output: 'A'

# Attempting to modify the proxy (this will raise an error)
try:
    d_proxy[2] = 'x'
except TypeError as e:
    print(e)  # Output: 'mappingproxy' object does not support item assignment

# Modifying the original dictionary
d[2] = 'B'

# Changes in the original dictionary are reflected in the proxy
print(d_proxy)  # Output: mappingproxy({1: 'A', 2: 'B'})
print(d_proxy[2])  # Output: 'B'
```

### Explanation

- **Creating a MappingProxy**:
    ```python
    from types import MappingProxyType
    d = {1: 'A'}
    d_proxy = MappingProxyType(d)
    ```

- **Accessing Items**:
    ```python
    print(d_proxy[1])  # Output: 'A'
    ```

- **Attempting to Modify the Proxy**:
    ```python
    try:
        d_proxy[2] = 'x'
    except TypeError as e:
        print(e)  # Output: 'mappingproxy' object does not support item assignment
    ```

- **Modifying the Original Dictionary**:
    ```python
    d[2] = 'B'
    print(d_proxy[2])  # Output: 'B'
    ```

### Use Case in Hardware Programming

In a hardware programming scenario, the constructor in a concrete `Board` subclass could fill a private mapping with the pin objects and expose it to clients of the API via a public `.pins` attribute implemented as a `mappingproxy`. This ensures that clients cannot add, remove, or change pins by accident.

```python
class Board:
    def __init__(self):
        self._pins = {1: 'Pin1', 2: 'Pin2'}  # Private mapping
        self.pins = MappingProxyType(self._pins)  # Public read-only proxy

# Example usage
board = Board()
print(board.pins[1])  # Output: 'Pin1'

# Attempting to modify the proxy (this will raise an error)
try:
    board.pins[3] = 'Pin3'
except TypeError as e:
    print(e)  # Output: 'mappingproxy' object does not support item assignment

# Modifying the private mapping
board._pins[3] = 'Pin3'
print(board.pins[3])  # Output: 'Pin3'
```

## Conclusion

`MappingProxyType` is a useful tool for creating read-only but dynamic views of dictionaries. This can be particularly valuable in scenarios where the integrity of the mapping needs to be preserved, such as in hardware programming where mappings represent immutable physical components.
