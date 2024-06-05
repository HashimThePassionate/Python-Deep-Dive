class GenericList:
    def __init__(self):
        self.items = []
        self.count = 0

    def add(self, item):
        self.items.append(item)
        self.count += 1

    def get(self, index):
        return self.items[index]

    def __iter__(self):
        return self.ListIterator(self)

    class ListIterator:
        def __init__(self, generic_list):
            self._generic_list = generic_list
            self._index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self._index < self._generic_list.count:
                item = self._generic_list.items[self._index]
                self._index += 1
                return item
            else:
                raise StopIteration

list = GenericList()
list.add('Muhammad')
list.add('Hashim')

for item in list:
    print(item)
