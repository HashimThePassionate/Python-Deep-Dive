class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) < (other.x, other.y)

    def __le__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) <= (other.x, other.y)

    def __gt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) > (other.x, other.y)

    def __ge__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) >= (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

# Creating two Point objects
point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(0, 3)

# Testing the comparison methods
print(point1 == point2)  # True
print(point1 != point2)  # False
print(point1 < point3)   # False
print(point1 <= point3)  # False
print(point1 > point3)   # True
print(point1 >= point3)  # True
print(point1 == point3)  # False
print(point1 != point3)  # True

# Testing the identity comparison
print(point1 is point2)  # False, as 'is' checks for identity not equality

# Testing the hash method
print(hash(point1))
print(hash(point2))
print(hash(point3))
