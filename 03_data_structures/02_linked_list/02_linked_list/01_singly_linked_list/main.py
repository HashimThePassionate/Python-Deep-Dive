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

    def iter(self):
        """Yield each data item in the list."""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def append(self, data):
        node = Node(data=data)
        if self.tail:
            self.tail.next = node
            self.tail = node
            self.size += 1
        else:
            self.head = node
            self.tail = node
            self.size += 1

    def append_at_a_location(self, data, index):
        if index < 1:
            print('Index should be greater than 1')
            return

        node = Node(data)

        # Case 1: Insert at head
        if index == 1:
            node.next = self.head
            self.head = node
            if self.tail is None:  # if list was empty
                self.tail = node
            self.size += 1
            return

        # Case 2: Insert at any middle or end position
        current = self.head
        prev = None
        count = 1

        while current:
            if count == index:
                prev.next = node
                node.next = current
                self.size += 1
                return
            prev = current
            current = current.next
            count += 1

        # Case 3: If inserting at the end (index == size + 1)
        if count == index:
            prev.next = node
            self.tail = node
            self.size += 1
        else:
            print("The list has fewer than {} elements".format(index))

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

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def delete_first_node(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        node_to_delete = self.head
        deleted_data = node_to_delete.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return deleted_data

    def delete_last_node(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        current = self.head
        prev = None
        if current.next is None:
            deleted_data = current.data
            self.head = None
            self.tail = None
            self.size -= 1
            return deleted_data

        while current.next:
            prev = current
            current = current.next

        deleted_data = current.data
        prev.next = None
        self.tail = prev
        self.size -= 1
        return deleted_data

    def delete_at_a_location(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                if current.next is None:
                    self.tail = prev
                self.size -= 1
                return current
            prev = current
            current = current.next
        return None

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0



# -------------------------------------------------------------------------
#  Assuming we have a linked list with the elements 'eggs', 'ham', and 'spam':
# words = SinglyLinkedList()
# words.append('eggs')
# words.append('ham')
# words.append('spam')


# -------------------------------------------------------------------------
# Display the linked list
# current = words.head
# while current:
#     print(current.data)
#     current = current.next


# -------------------------------------------------------------------------
# Insert 'new' at index 2
# This will insert 'new' between 'eggs' and 'ham'
# words.append_at_a_location('new', 2)


# -------------------------------------------------------------------------
# # Display the linked list after insertion
# current = words.head
# while current:
#     print(current.data)
#     current = current.next


# -------------------------------------------------------------------------
# Insert 'new' at index 1 (head)
# words.append_with_same_data('spam')
# # Display the linked list after insertion
# current = words.head
# while current:
#  print(current.data)
#  current = current.next


# -------------------------------------------------------------------------
# Search for 'ham' in the linked list
# node = words.search('ham')
# if node:
#     print(f"Found node with data: {node.data}")
# else:
#     print("Node not found.")


# -------------------------------------------------------------------------
# Delete the first node
# print("Before deletion:", list(words.iter()))
# deleted = words.delete_first_node()
# print(f"Deleted: {deleted}")
# print("After deletion:", list(words.iter()))


# -------------------------------------------------------------------------
# Create a new linked list and append some elements
# words = SinglyLinkedList()
# words.append(1)
# words.append(5)
# words.append(2)
# words.append(8)

# print("Before:", list(words.iter()))
# # → [1, 5, 2, 8]
# # Delete the last node
# deleted = words.delete_last_node()
# print(f"Deleted: {deleted}")
# # → 8

# print("After:", list(words.iter()))
# ---------------------------------------------------------------------------
# Create a new linked list, append some elements and delete a specific node
words = SinglyLinkedList()
words.append('eggs')
words.append('ham')
words.append('spam')
print("Before deletion:", list(words.iter()))
words.delete_at_a_location('ham')
print("After deletion:", list(words.iter()))
words.clear()
print("After clearing:", list(words.iter()))
