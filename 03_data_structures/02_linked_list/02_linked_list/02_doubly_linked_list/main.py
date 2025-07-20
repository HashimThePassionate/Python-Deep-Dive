class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
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
    def append_at_index(self, index, data):
        # 1. Bounds check
        if index < 1:
            print("❌ Index should be 1 or greater.")
            return

        new_node = Node(data, None, None)

        # 2. Insert at head
        if index == 1:
            if not self.head:  # empty list
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

        # 3. Insert at tail
        elif index == self.count:
            new_node.prev = self.tail
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node

        # 4. Insert in the middle
        else:
            # traverse to the node currently at position `index`
            current = self.head
            for _ in range(index):
                current = current.next
            # now `current` is the node that will come after new_node
            prev_node = current.prev

            prev_node.next = new_node
            new_node.prev = prev_node

            new_node.next = current
            current.prev = new_node

        self.count += 1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next 
            yield val
    
    def contains(self, data):
        for node_data in self.iter():
            if data == node_data:
                print(f"Data item is present in the list. i.e {data}")
                return
        print(f"Data item is not present in the list. i.e {data}")
    
    def delete(self, data):
        current = self.head
        node_deleted = False
        if current is None:
            print("List is empty. Nothing to delete.")
            return
        elif current.data == data:
            self.head.prev = None
            node_deleted = True
            self.head = current.next
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                    break
                current = current.next

        if node_deleted:
            print(f"Node with data {data} deleted successfully.")
            self.count -= 1

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
# words = DouplyLinkedList()
# words.append('egg')
# words.append('ham') 
# words.append('spam')

# words.append_at_a_location('ham')

# print("Doubly linked list after adding an element after word \"ham\" inthe list.")

# current = words.head
# while current:
#  print(current.data)
#  current = current.next


# Searching Element
# words = DouplyLinkedList()
# words.append('egg')
# words.append('ham') 
# words.append('spam')
# words.contains("ham")
# words.contains("ham2")



#   Deleting Element
words = DoublyLinkedList()
words.append('egg')   # List: egg
words.append('ham')   # List: egg <-> ham
words.append('spam')  # List: egg <-> ham <-> spam

# before deletion
current = words.head
print("Doubly linked list before deletion:")
while current:
 print(current.data)
 current = current.next

words.delete('ham')

# after deletion
current = words.head
print("Doubly linked list after deletion:")
while current:
 print(current.data)
 current = current.next