class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DouplyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 1

    def append(self, data):
        # Append an item at the end of the list.
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def append_at_start(self, data):
        new_node = Node(data, next=None, prev=None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1


# 1️⃣ Create list and append some items (using previously defined append)
words = DouplyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

# 2️⃣ Display before insertion at start
print("Before append_at_start:")
current = words.head
while current:
    print(current.data)
    current = current.next

# 3️⃣ Insert at beginning
words.append_at_start('book')

# 4️⃣ Display after insertion
print("\nAfter append_at_start:")
current = words.head
while current:
    print(current.data)
    current = current.next
