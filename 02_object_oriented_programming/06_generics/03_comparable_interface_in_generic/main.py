class ComparableObject:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if isinstance(other, ComparableObject):
            return self.value < other.value
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, ComparableObject):
            return self.value <= other.value
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, ComparableObject):
            return self.value == other.value
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, ComparableObject):
            return self.value != other.value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, ComparableObject):
            return self.value > other.value
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, ComparableObject):
            return self.value >= other.value
        return NotImplemented

# Example usage:
obj1 = ComparableObject(10)
obj2 = ComparableObject(20)

print(obj1 < obj2)  # True
print(obj1 <= obj2) # True
print(obj1 == obj2) # False
print(obj1 != obj2) # True
print(obj1 > obj2)  # False
print(obj1 >= obj2) # False
