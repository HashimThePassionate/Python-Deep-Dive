# Queue implementation using a list
class ListQueue:
    def __init__(self):
        self.items = []
        self.front = self.rear = 0
        self.size = 3

    def enqueue(self, data):
        if self.size == self.rear:
            print("Queue is full")
            return
        self.items.append(data)
        self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print('Queue is empty')
        else:
            data = self.items.pop(0)
            self.rear -= 1
            return data


# q = ListQueue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# print(f"Enqueued: {q.items}")
# data = q.dequeue()
# print(f"Dequeued: {data}")
# print(f"Dequeued: {q.items}")
# q.dequeue()
# print(f"Dequeued: {q.items}")
# q.dequeue()
# print(f"Dequeued: {q.items}")


# Queue implementation using a doubly linked list
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = Node(data, None, None)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            data = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return data
        elif self.count < 1:
            print('Queue is empty')
        self.count -= 1
    
    def iter(self):
        current = self.head
        while current:
            yield current
            current = current.next


# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)

# for n in q.iter():
#     print(f"Data: {n.data}")

# print(f"Enqueued: {q.head.data}, {q.tail.data}")

# data = q.dequeue()
# print(f"Dequeued: {data}")

# for n in q.iter():
#     print(f"Data: {n.data}")

# data = q.dequeue()
# print(f"Dequeued: {data}")

# for n in q.iter():
#     print(f"Data: {n.data}")



class Queue:
    def __init__(self):
        self.Stack1 = []
        self.Stack2 = []

    def enqueue(self, data):
        self.Stack1.append(data)
    
    def dequeue(self):
        if not self.Stack2:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
        if not self.Stack2:
            print("No Element to dequeue")
            return
        return self.Stack2.pop()


queue = Queue()
queue.enqueue(23)
queue.enqueue(13)
queue.enqueue(11)
print(queue.Stack1)

queue.dequeue()
print(queue.Stack2)