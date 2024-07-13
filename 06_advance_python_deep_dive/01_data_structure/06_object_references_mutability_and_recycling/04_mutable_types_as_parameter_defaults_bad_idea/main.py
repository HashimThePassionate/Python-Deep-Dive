class HauntedBus:
    """A bus model haunted by ghost passengers"""
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)  # Output: ['Alice', 'Bill']

bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)  # Output: ['Bill', 'Charlie']


bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)  # Output: ['Carrie']

bus3 = HauntedBus()
print(bus3.passengers)  # Output: ['Carrie']

bus3.pick('Dave')
print(bus2.passengers)  # Output: ['Carrie', 'Dave']

print(bus2.passengers is bus3.passengers)  # Output: True
print(bus1.passengers)  # Output: ['Bill', 'Charlie']


print('-' * 50)
print(dir(HauntedBus.__init__))  # doctest: +ELLIPSIS
# Output: ['__annotations__', '__call__', ..., '__defaults__', ...]
print('-' * 50)
print(HauntedBus.__init__.__defaults__)  
# Output: (['Carrie', 'Dave'],)
print('-' * 50)
print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)  
# Output: True