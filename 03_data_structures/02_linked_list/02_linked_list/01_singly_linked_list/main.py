class Node:
    def __init__(self, data=None):
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

    def append_at_a_location(self, data, index):
        if index < 1:
            print("Index should be 1 or greater. ")
            return
        node = Node(data)
        # Case 1: Insert at the head
        if index == 1:
            node.next = self.head
            self.head = node
            return
        # For index > 1, walk the list looking for the insertion point
        current = self.head
        prev = None
        count = 1
        while current:
            if count == index:
                prev.next = node
                node.next = current
                return
            prev = current
            current = current.next
            count += 1
        # If we exit the loop with count < index, list was too short
        if count < index:
            print("The list has fewer than {} elements".format(index))
        else:
            # count == index here means we fell off exactly at tail,
            # so append at end:
            prev.next = node

    def append_with_same_data(self, data):
        current = self.head
        prev = self.head
        node = Node(data)
        while current:
            if current.data == data:
                node.next = current
                prev.next = node
            prev = current
            current = current.next


words = SinglyLinkedList()
words.append('eggs')
words.append('ham')
words.append('spam')

# current = words.head
# while current:
#     print(current.data)
#     current = current.next

words.append_at_a_location('new', 2)

current = words.head
while current:
    print(current.data)
    current = current.next

words.append_with_same_data('spam')
# current = words.head
# while current:
#  print(current.data)
#  current = current.next
