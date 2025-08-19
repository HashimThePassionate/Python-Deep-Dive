class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def is_op(x: str) -> bool:
    return x in "+-*/"

def precedence(op: str) -> int:
    # higher number => higher precedence
    return {"+": 1, "-": 1, "*": 2, "/": 2}.get(op, 0)

def is_left_assoc(op: str) -> bool:
    # All four are left-associative here
    return True


def calc(node: TreeNode):
    if node is None:
        return 0
    if not is_op(str(node.data)):
        return node.data
    a = calc(node.left)
    b = calc(node.right)
    if node.data == "+": return a + b
    if node.data == "-": return a - b
    if node.data == "*": return a * b
    if node.data == "/": return a / b

def to_postfix(node: TreeNode) -> str:
    if not node: return ""
    if not is_op(str(node.data)): return str(node.data)
    return f"{to_postfix(node.left)} {to_postfix(node.right)} {node.data}".strip()

def to_prefix(node: TreeNode) -> str:
    if not node: return ""
    if not is_op(str(node.data)): return str(node.data)
    return f"{node.data} {to_prefix(node.left)} {to_prefix(node.right)}".strip()

def to_infix(node: TreeNode) -> str:
    if not node: return ""
    if not is_op(str(node.data)): return str(node.data)
    # Parenthesize to preserve structure
    return f"({to_infix(node.left)} {node.data} {to_infix(node.right)})"

def build_from_postfix(postfix: str) -> TreeNode:
    stack = []
    for tok in postfix.split():
        if is_op(tok):
            right = stack.pop()
            left  = stack.pop()
            node = TreeNode(tok)
            node.left, node.right = left, right
            stack.append(node)
        else:
            stack.append(TreeNode(int(tok)))
    return stack.pop()

def build_from_prefix(prefix: str) -> TreeNode:
    stack = []
    tokens = prefix.split()[::-1]  # scan right → left
    for tok in tokens:
        if is_op(tok):
            left  = stack.pop()   # first pop = left
            right = stack.pop()   # second pop = right
            node = TreeNode(tok)
            node.left, node.right = left, right
            stack.append(node)
        else:
            stack.append(TreeNode(int(tok)))
    return stack.pop()


def build_from_infix(infix: str) -> TreeNode:
    nodes, ops = [], []

    i, n = 0, len(infix)
    def reduce_once():
        op = ops.pop()
        right = nodes.pop()
        left  = nodes.pop()
        node = TreeNode(op)
        node.left, node.right = left, right
        nodes.append(node)

    while i < n:
        ch = infix[i]

        # Skip spaces
        if ch.isspace():
            i += 1
            continue

        # Number (supports multi-digit)
        if ch.isdigit():
            j = i
            while j < n and (infix[j].isdigit()):
                j += 1
            nodes.append(TreeNode(int(infix[i:j])))
            i = j
            continue

        # Parentheses
        if ch == '(':
            ops.append(ch)
            i += 1
            continue

        if ch == ')':
            while ops and ops[-1] != '(':
                reduce_once()
            ops.pop()  # pop '('
            i += 1
            continue

        # Operator
        if is_op(ch):
            while (ops and is_op(ops[-1]) and
                   (precedence(ops[-1]) > precedence(ch) or
                    (precedence(ops[-1]) == precedence(ch) and is_left_assoc(ch)))):
                reduce_once()
            ops.append(ch)
            i += 1
            continue

        raise ValueError(f"Unexpected token: {ch!r}")

    # Final reductions
    while ops:
        reduce_once()

    return nodes.pop()


# Postfix
root_post = build_from_postfix("4 5 + 5 3 - *")
print(to_prefix(root_post))  # * + 4 5 - 5 3
print(to_infix(root_post))   # ((4 + 5) * (5 - 3))
print(calc(root_post))       # 18

# Prefix
root_pre = build_from_prefix("* + 4 5 - 5 3")
print(to_postfix(root_pre))  # 4 5 + 5 3 - *
print(to_infix(root_pre))    # ((4 + 5) * (5 - 3))
print(calc(root_pre))        # 18

# Infix
root_in = build_from_infix("(4 + 5) * (5 - 3)")
print(to_prefix(root_in))    # * + 4 5 - 5 3
print(to_postfix(root_in))   # 4 5 + 5 3 - *
print(calc(root_in))         # 18