import copy
class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print(f'id(bus1)={id(bus1)}, id(bus2)={id(bus2)}, id(bus3)={id(bus3)}')
# Output: id(bus1)=2294379765664, id(bus2)=2294379861856, id(bus3)=2294379861952

bus1.drop('Bill')
print(bus2.passengers)  # Output: ['Alice', 'Claire', 'David']

print(f'id(bus1)={id(bus1)}, id(bus2)={id(bus2)}, id(bus3)={id(bus3)}')
# Output: id(bus1)=2294379765664, id(bus2)=2294379861856, id(bus3)=2294379861952

print(bus3.passengers)  # Output: ['Alice', 'Bill', 'Claire', 'David']