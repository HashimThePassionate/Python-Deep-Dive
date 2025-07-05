class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

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
            self.tail =  node
    
    def append_at_a_location(self, data, index):
        node = Node(data)
        current = self.head
        prev = self.head
        count = 1
        while current:
            if count == 1:
                node.next = current
                self.head = node
                print(count)
                return
            elif index == count:
                node.next = current
                prev.next = node
                return
            count += 1
            prev = current
            current = current.next
            