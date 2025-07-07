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
words = SinglyLinkedList()
words.append(1)
words.append(5)
words.append(2)
words.append(8)

print("Before:", list(words.iter()))
# → [1, 5, 2, 8]

deleted = words.delete_last_node()
print(f"Deleted: {deleted}")
# → 8

print("After:", list(words.iter()))