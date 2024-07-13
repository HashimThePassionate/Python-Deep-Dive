a = [1, 2]
b = a
del a
print(b)  # Output: [1, 2]
b = [3]


class Resource:
    def __init__(self, name):
        self.name = name
        print(f'Resource {self.name} created')

    def __del__(self):
        print(f'Resource {self.name} destroyed')

# Usage
r = Resource('A')
del r  # Output: Resource A destroyed



import weakref

s1 = {1, 2, 3}
s2 = s1

def bye():
    print('...like tears in the rain.')

ender = weakref.finalize(s1, bye)
print(ender.alive)  # Output: True

del s1
print(ender.alive)  # Output: True

s2 = 'spam'
# Output: ...like tears in the rain.
print(ender.alive)  # Output: False