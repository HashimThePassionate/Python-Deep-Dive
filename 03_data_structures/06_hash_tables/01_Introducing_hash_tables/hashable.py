class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0
        self.MAXLOADFACTOR = 0.65

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

    def check_growth(self):
        loadfactor = self.count / self.size
        if loadfactor > self.MAXLOADFACTOR:
            print("Load factor before growing the hash table", self.count
                  / self.size)
            self.growth()
            print("Load factor after growing the hash table", self.count /
                  self.size)

    def growth(self):
        New_Hash_Table = HashTable()
        New_Hash_Table.size = 2 * self.size
        New_Hash_Table.slots = [None for i in range(New_Hash_Table.size)]

        for i in range(self.size):
            if self.slots[i] != None:
                New_Hash_Table.put(self.slots[i].key, self.slots[i].value)
        self.size = New_Hash_Table.size
        self.slots = New_Hash_Table.slots
    
    def get(self,key):
        h = self._hash(key)
        while self.slots[h] != None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + 1) % self.size
        return None
    
    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        return self.get(key)


# ht = HashTable()
# ht.put("good", "eggs")
# ht.put("better", "ham")
# ht.put("best", "spam")
# ht.put("ad", "do not")
# ht.put("ga", "collide")
# ht.put("awd", "do not")
# ht.put("add", "do not")
# ht.check_growth()


# get key 
ht = HashTable()
# ht.put("good", "eggs")
# ht.put("better", "ham")
# ht.put("best", "spam")
# ht.put("ad", "do not")
# ht.put("ga", "collide")
ht["good"] = "eggs"
ht["better"] = "ham"
ht["best"] = "spam"
ht["ad"] = "do not"
ht["ga"] = "collide"

for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = v = ht[key]
    print(f'"{key}": "{v}"')
print("The number of elements is: {}".format(ht.count))