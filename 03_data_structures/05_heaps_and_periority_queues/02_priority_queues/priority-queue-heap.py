class PriorityQueueHeap:
    def __init__(self):
        self.heap = [()]
        self.size = 0
    
    def arrange(self, i):
        while i // 2 > 0:
            if self.heap[i][0] < self.heap[i // 2][0]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2
    
    def insert(self, priority, item):
        self.heap.append((priority, item))
        self.size += 1
        self.arrange(self.size)
    
    def sink(self, i):
        while i * 2 <= self.size:
            mc = self.minchild(i)
            if self.heap[i][0] > self.heap[mc][0]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc
    
    def minchild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i * 2][0] < self.heap[i * 2 + 1][0]:
            return i * 2
        return i * 2 + 1
    
    def delete_at_root(self):
        item = self.heap[1][1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item


h = PriorityQueueHeap()
h.insert(2, "Bat")
h.insert(13,"Cat")
h.insert(18, "Rat")
h.insert(26, "Ant")
h.insert(3, "Lion")
h.insert(4, "Bear")
# h.heap


for i in range(h.size):
    n = h.delete_at_root()
    print(n)
    print(h.heap)