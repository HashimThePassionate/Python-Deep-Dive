class Stack:
    def __init__(self):
        self.elements = []
    def push(self, item):
        self.elements.append(item)
    def pop(self):
        return self.elements.pop()

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def calc(node):
    if node.data == "+":
        return calc(node.left) + calc(node.right)
    elif node.data == "-":
        return calc(node.left) - calc(node.right)
    elif node.data == "*":
        return calc(node.left) * calc(node.right)
    elif node.data == "/":
        return calc(node.left) / calc(node.right)
    else:
        return node.data

# ---------- PREFIX PARSING (Right-to-Left, using a stack) ----------
def build_tree_from_prefix(prefix_tokens):
    st = Stack()
    for tok in reversed(prefix_tokens):
        if tok in "+-*/":
            node = TreeNode(tok)
            left_child = st.pop()
            right_child = st.pop()
            node.left = left_child
            node.right = right_child
            st.push(node)
        else:
            st.push(TreeNode(int(tok)))
    return st.pop()

# Example
prefix_expr = "* + 4 5 - 5 3".split()
root = build_tree_from_prefix(prefix_expr)
print(calc(root))  # -> 18