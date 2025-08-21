class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


class Tree:
    def __init__(self):
        self.root_node = None
    
    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return self.root_node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return self.root_node
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return self.root_node
    
    def search(self,data):
        current = self.root_node
        while True:
            if current is None:
                print("Item Not Found")
                return None
            elif current.data == data:
                print(f'Item Found: {data}')
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child
    
    def in_order_traversal(self, root_node):
        current = root_node
        if current is None:
            return
        self.in_order_traversal(current.left_child)
        print(current.data)
        self.in_order_traversal(current.right_child)

# tree = Tree()
# r = tree.insert(5)
# r = tree.insert(2)
# r = tree.insert(7)
# r = tree.insert(9)
# r = tree.insert(1)
# tree.in_order_traversal(tree.root_node)


# Searching data
tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)

print(tree.search(9))  
