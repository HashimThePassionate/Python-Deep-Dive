class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.head = self.tail = new_node
            self.tail.next = self.head
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

    def delete(self, data):
        current = self.head
        previous = self.head
        flag = False
        while previous == current or previous != self.tail:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                    print(f"Deleted item = {data}")
                elif current == self.tail:
                    self.tail = previous
                    self.tail.next = self.head
                    print(f"Deleted item = {data}")
                else:
                    previous.next = current.next
                    print(f"Deleted item = {data}")
                self.size -= 1
                return
            previous = current
            current = current.next
        if flag is False:
                print(f"Item not present in the list = {data}")

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


# Appending and iterating through the circular linked list
# words = CircularLinkedList()
# words.append('spam')
# words.append('ham')
# words.append('eggs')
# words.append_at_a_location('bacon', 2)

# counter = 0
# for word in words.iter():
#     print(word)
#     counter += 1
#     if counter > 4:
#         break


# delete a node from the circular linked list
words = CircularLinkedList()
words.append('eggs')
words.append('ham')
words.append('spam')
words.append('foo')
words.append('bar')
print("Let us try to delete something that isn't in the list.")
words.delete('socks')
counter = 0
for item in words.iter():
    print(item)
    counter += 1
    if counter > 4:
        break


print("Let us delete something that is there.")
words.delete('foo')
counter = 0
for item in words.iter():
    print(item)
    counter += 1
    if counter > 3:
        break
