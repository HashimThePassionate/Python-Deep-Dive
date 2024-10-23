import user
import sys

for path in sys.path:
    print(path)


import helper
name = helper.get_name()
myname = user.username(name)
print(myname)