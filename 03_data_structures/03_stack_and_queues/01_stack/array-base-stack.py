size = 3
data = [None] * size
top = -1


def push(value):
    global top
    if top >= size - 1:
        print("Stack overflow")
    else:
        top = top + 1
        data[top] = value

def pop():
    global top
    if top == -1:
        print("Stack Underflow")
        return None
    else:
        value = data[top]
        data[top] = None
        top -= 1
        return value

def peek():
    global top
    if top == -1:
        print("Stack is empty")
        return None
    else:
        return data[top]


push('egg')
push('ham')
push('spam')

print(data[0:top+1])

push('bacon')
push('sausage')

print(data[0:top+1])

print(pop())
print(data[0:top+1])

print(pop())
print(data[0:top+1])

print('Peek:', peek())

print(pop())
print(data[0:top+1])

print(pop())
print(data[0 : top + 1])