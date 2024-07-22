from typing import Any

class T1:
    def method(self):
        print("T1 method")

class T2(T1):
    def method(self):
        print("T2 method")

def f1(p: T1) -> None:
    p.method()

# o2 = T2()
# f1(o2)  # OK because T2 is a subtype of T1

def f2(p: T2) -> None:
    p.method()

# o1 = T1()
# f2(o1)  # Type error because T1 is not a subtype of T2

from typing import Any

def f3(p: Any) -> None:
    print(p)

o0 = object()
o1 = T1()
o2 = T2()
f3(o0)  # OK: rule #2
f3(o1)  # OK: rule #2
f3(o2)  # OK: rule #2

def f4() -> Any:  # implicit return type: `Any`
    return "example"

o4 = f4()  # inferred type: `Any`
f3(o4)  # OK: rule #3
# f1(o4)  # Raises AttributeError at runtime
# f2(o4)  # Raises AttributeError at runtime
