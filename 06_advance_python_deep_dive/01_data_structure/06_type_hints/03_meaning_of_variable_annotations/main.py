from demo_plain import DemoPlainClass, DemoNTClass, DemoDataClass

print(DemoPlainClass.__annotations__)
# Output: {'a': <class 'int'>, 'b': <class 'float'>}

print(DemoPlainClass.b)
# Output: 1.1

print(DemoPlainClass.c)
# Output: 'spam'

try:
    print(DemoPlainClass.a)
except AttributeError as e:
    print(e)
# Output: AttributeError: type object 'DemoPlainClass' has no attribute 'a'



# ---------------------------------------------------------
print("---------------------------------------------------------")
print(DemoNTClass.__annotations__)
# Output: {'a': <class 'int'>, 'b': <class 'float'>}
print('b------------------------')
print(DemoNTClass.b)
# Output: 1.1

print('c------------------------')
print(DemoNTClass.c)
# Output: 'spam'

print('c------------------------')
try:
    print(DemoNTClass.a)
except AttributeError as e:
    print(e)
# Output: _collections._tuplegetter object at 0x...

# Demo Data Class
# ---------------------------------------------------------
print("---------------------------------------------------------")
nt = DemoNTClass(8)
print(nt.a)
# Output: 8

print(nt.b)
# Output: 1.1

print(nt.c)
# Output: 'spam'

print(DemoDataClass.__annotations__)
# Output: {'a': <class 'int'>, 'b': <class 'float'>}

print(DemoDataClass.__doc__)
# Output: 'DemoDataClass(a: int, b: float = 1.1)'

print(DemoDataClass.b)
# Output: 1.1

print(DemoDataClass.c)
# Output: 'spam'

try:
    print(DemoDataClass.a)
except AttributeError as e:
    print(e)
# Output: AttributeError: type object 'DemoDataClass' has no attribute 'a'

dc = DemoDataClass(9)
print(dc.a)
# Output: 9

print(dc.b)
# Output: 1.1

print(dc.c)
# Output: 'spam'

# Mutability demonstration
dc.a = 10
print(dc.a)
# Output: 10

# dc.b = 'oops'
print(dc.b)
# Output: 'oops'

dc.c = 'whatever'
print(dc.c)
# Output: 'whatever'

# dc.z = 'secret stash'
# print(dc.z)
# Output: 'secret stash'