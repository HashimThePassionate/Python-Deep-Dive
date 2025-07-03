class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

    def iter(self):
        current = self
        while current:
            val = current.data
            current = current.next
            yield val

# n1 : Node = Node('eggs')
# n2 : Node = Node('ham')
# n3 : Node = Node('spam')

# n1.next = n2
# n2.next = n3

# current = n1

# for value in current.iter():
#     print(value)

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node 
            self.tail = node

words = SinglyLinkedList()
words.append('eggs')
words.append('ham')
words.append('spam')

current = words.head
while current:
    print(current.data)
    current = current.next