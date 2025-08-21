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
    
    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        while current is not None:
            if current.data == data:
                return (parent, current)
            parent = current
            if data < current.data:
                current = current.left_child
            else:
                current = current.right_child
        return (parent, None) 

    
    def remove(self, data):
        parent, node = self.get_node_with_parent(data)
        if node is None:
            print("Not found:", data)
            return False

        # Count children
        left = node.left_child
        right = node.right_child
        if left and right:
            children_count = 2
        elif left is None and right is None:
            children_count = 0
        else:
            children_count = 1

        # Case 0: leaf
        if children_count == 0:
            if parent is None:
                self.root_node = None
            else:
                if parent.left_child is node:
                    parent.left_child = None
                else:
                    parent.right_child = None
            return True

        # Case 1: one child
        if children_count == 1:
            next_node = left if left else right
            if parent is None:
                self.root_node = next_node
            else:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            return True

        # Case 2: two children
        parent_of_leftmost = node
        leftmost = node.right_child
        while leftmost.left_child:
            parent_of_leftmost = leftmost
            leftmost = leftmost.left_child

        # Copy value into node
        node.data = leftmost.data

        # Remove the leftmost from its original place
        if parent_of_leftmost.left_child is leftmost:
            parent_of_leftmost.left_child = leftmost.right_child
        else:
            parent_of_leftmost.right_child = leftmost.right_child

        return True


    
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
# tree = Tree()
# tree.insert(5)
# tree.insert(2)
# tree.insert(7)
# tree.insert(9)
# tree.insert(1)

# print(tree.search(9))  


# Deleting data
tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)
tree.search(9)
print(tree.remove(9))
tree.search(9)