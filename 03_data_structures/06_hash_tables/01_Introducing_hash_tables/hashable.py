class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0

    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size
    
    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        while self.slots[h] != None:
            if self.slots[h].key == key:
                break
            h = (h + 1) % self.size
        if self.slots[h] == None:
            self.count += 1
        self.slots[h] = item
        self.check_growth()

