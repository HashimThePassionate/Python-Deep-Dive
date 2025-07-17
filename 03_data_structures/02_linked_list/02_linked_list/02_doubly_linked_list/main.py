class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DouplyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
        self.count += 1

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1


words = DouplyLinkedList()
words.append_at_start('book')
# print(words.head.data)  # Output: 'book'
# print(words.tail.data)  # Output: 'book'
# print(words.count)
words.append('egg')
current = words.head
while current:
 print(current.data)
 current = current.next