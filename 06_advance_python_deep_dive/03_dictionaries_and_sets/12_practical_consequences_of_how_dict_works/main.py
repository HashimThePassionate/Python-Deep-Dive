class HashableObject:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)  # Returns the hash value of the value

    def __eq__(self, other):
        return self.value == other.value  # Checks if two objects are equal

key = HashableObject(10)
d = {key: 'value'}  # Using the hashable object as a key in a dictionary
print(d[key])  # Output: 'value'



class MyClass:
    def __init__(self, value):
        self.value = value  # Attribute created in __init__

obj = MyClass(10)
print(obj.__dict__)  # Output: {'value': 10}



