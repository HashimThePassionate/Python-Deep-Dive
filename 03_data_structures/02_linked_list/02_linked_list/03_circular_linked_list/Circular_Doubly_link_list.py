class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self.count += 1

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
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
            self.append_at_start(data)

        # 3. Insert at tail
        elif index == self.count + 1:
            self.append(data)

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
        if not self.head:
            return
        current = self.head
        for _ in range(self.count):  # count tak hi chalay loop
            yield current.data
            current = current.next

    def contains(self, data):
        for node_data in self.iter():
            if data == node_data:
                print(f"Data item is present in the list. i.e {data}")
                return
        print(f"Data item is not present in the list. i.e {data}")

    def delete(self, data):
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        found = False
        for _ in range(self.count):
            if current.data == data:
                found = True
                break
            current = current.next

        if not found:
            print("Data not found.")
            return

        if self.count == 1:
            self.head = self.tail = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            if current == self.head:
                self.head = current.next
            if current == self.tail:
                self.tail = current.prev

        self.count -= 1
        print(f"Node with data {data} deleted successfully.")
