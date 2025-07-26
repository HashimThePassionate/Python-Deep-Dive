class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None  

class stack:  
    def __init__(self):  
        self.top = None  
        self.size = 0  

    def push(self, data):  
        node = Node(data)  
        node.next = self.top  
        self.top = node  
        self.size += 1 

    def pop(self):  
        if not self.top: return None  
        data = self.top.data  
        self.top = self.top.next  
        self.size -= 1  
        return data  

def check_brackets(expression):
    brackets_stack = stack()
    last = ' '
    for ch in expression:
        if ch in ('{', '[', '('):
            brackets_stack.push(ch)
        if ch in ('}', ']', ')'):
            last = brackets_stack.pop()
            if last == '{' and ch == '}':
                continue
            elif last == '[' and ch == ']':
                continue
            elif last == '(' and ch == ')':
                continue
            else:
                return False
    if brackets_stack.size > 0:
        return False
    else:
         return True

# sl = (
#  "{(foo)(bar)}[hello](((this)is)a)test",
#  "{(foo)(bar)}[hello](((this)is)atest",
#  "{(foo)(bar)}[hello](((this)is)a)test))"
# )
# for s in sl:
#  m = check_brackets(s)
#  print("{}: {}".format(s, m))


def check_brackets(expr):
    s = stack()
    open_c = matched = 0
    remarks = []

    for ch in expr:
        if ch in '{[(':
            s.push(ch); open_c += 1
        elif ch in '}])':
            last = s.pop()
            if last is None:
                remarks.append(f"Extra closing: {ch}")
            elif (last + ch) in ['{}', '[]', '()']:
                matched += 1
            else:
                remarks.append(f"Mismatch: {last} vs {ch}")

    if s.size > 0:
        remarks.append(f"{s.size} opening(s) not closed")

    return {
        "Open": open_c,
        "Matched": matched,
        "Unmatched": s.size,
        "Remarks": remarks or ["✅ All matched"]
    }

 

def check_brackets(expression):
    brackets_stack = stack()
    opening_count = 0
    matched_pairs = 0
    mismatch_info = []

    for ch in expression:
        if ch in ('{','[','('):
            brackets_stack.push(ch)
            opening_count += 1
        elif ch in ('}',']',')'):
            last = brackets_stack.pop()
            if last is None:
                mismatch_info.append(f"Extra closing bracket: {ch}")
                continue
            if (last == '{' and ch == '}') or \
               (last == '[' and ch == ']') or \
               (last == '(' and ch == ')'):
                matched_pairs += 1
            else:
                mismatch_info.append(f"Mismatch: opened with {last}, closed with {ch}")

    remaining = brackets_stack.size

    if remaining > 0:
        mismatch_info.append(f"{remaining} opening bracket(s) not closed")

    # Output format
    result = {
        "Total Opening Brackets": opening_count,
        "Matched Pairs": matched_pairs,
        "Unmatched Opening Brackets": remaining,
        "Remarks": mismatch_info if mismatch_info else ["All brackets matched correctly ✅"]
    }
    return result


sl = (
    "{(foo)(bar)}[hello](((this)is)a)test",
    "{(foo)(bar)}[hello](((this)is)atest",
    "{(foo)(bar)}[hello](((this)is)a)test)))"
)

for s in sl:
    print(f"\nExpression: {s}")
    result = check_brackets(s)
    for k, v in result.items():
        if isinstance(v, list):
            for line in v:
                print(f"  → {line}")
        else:
            print(f"{k}: {v}")


