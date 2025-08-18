from collections import deque
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

print('-'*30)
print("In-order Traversal:")
inorder(A)
print('-'*30)

def pre_order(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    pre_order(current.left_child)
    pre_order(current.right_child)

print('-'*30)
print("Pre-order Traversal:")
pre_order(A)
print('-'*30)


def post_order(root_node):
    current = root_node
    if current is None:
        return
    post_order(current.left_child)
    post_order(current.right_child)
    print(current.data)


print("Post-order Traversal:")
post_order(A)
print('-'*30)

def level_order_traversal(rode_node):
    list_of_nodes = []
    traversal_queue = deque([rode_node])
    while len(traversal_queue) > 0:
        node = traversal_queue.popleft()
        list_of_nodes.append(node.data)
        if node.left_child:
            traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)
    return list_of_nodes


print("Level-order Traversal:")
print(level_order_traversal(A))
print('-'*30)

#     print(current.data)
#     current = current.left_child
