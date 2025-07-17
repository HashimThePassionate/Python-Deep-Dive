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

    def append_at_a_location(self, data):
        current = self.head
        prev = self.head
        new_node = Node(data, None, None)
        while current:
            if current.data == data:
                new_node.prev = prev
                new_node.next = current
                prev.next = new_node
                current.prev = new_node
                self.count += 1
            prev = current
            current = current.next


# words = DouplyLinkedList()
# Insert a at start
# words.append_at_start('book')
# # print(words.head.data)  # Output: 'book'
# # print(words.tail.data)  # Output: 'book'
# # print(words.count)

# Insert at end
# words.append('egg')
# current = words.head
# while current:
#     print(current.data)
#     current = current.next


# Insert at intermediate
words = DouplyLinkedList()
words.append('egg')
words.append('ham') 
words.append('spam')

words.append_at_a_location('ham')

print("Doubly linked list after adding an element after word \"ham\" inthe list.")

current = words.head
while current:
 print(current.data)
 current = current.next