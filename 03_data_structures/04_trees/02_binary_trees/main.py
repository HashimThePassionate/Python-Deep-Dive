class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


# n1 = Node('Root Node')
# n2 = Node('Left Child')
# n3 = Node('Right Child')
# n4 = Node('Left Grandchild')

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')

A.left_child = B
A.right_child = C
B.left_child = D
B.right_child = E
D.left_child = G
D.right_child = H
C.right_child = F

def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)


inorder(A)


# current = n1
# while current:
#     print(current.data)
#     current = current.left_child
