# BST Node
class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# BST class for each bucket
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return BSTNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value  # Update if key exists
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder(self):
        out = []
        self._inorder(self.root, out)
        return out

    def _inorder(self, node, out):
        if node:
            self._inorder(node.left, out)
            out.append((node.key, node.value))
            self._inorder(node.right, out)

# Hash Table with BST chaining
class HashTableBST:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.table = [BST() for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        self.table[index].insert(key, value)

    def get(self, key):
        index = self._hash(key)
        return self.table[index].search(key)

    def display(self):
        for i, bst in enumerate(self.table):
            print(f"Bucket {i}: {bst.inorder()}")

# ------------------------------
# Demo
# ------------------------------
if __name__ == "__main__":
    ht = HashTableBST()

    # Insert keys (collisions will be stored in BST of each bucket)
    for k in [10, 20, 15, 7, 22, 5, 30]:
        ht.put(k, f"val-{k}")

    ht.display()
    print("Get 15:", ht.get(15))
    print("Get 99:", ht.get(99))  # Not found
