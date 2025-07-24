class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data


class stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            print("Stack is already empty!")
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            print('Stack is empty!')


words = stack()
words.push('egg')
words.push('ham')
words.push('spam')

words.pop()
words.pop()
words.pop()
words.peek()
words.pop()

current = words.top
while current:
    print(current.data)
    current = current.next

