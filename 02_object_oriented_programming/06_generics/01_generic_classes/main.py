from typing import TypeVar, List

T = TypeVar('T')  # Declare a type variable 'T'


class GenericList:
    def __init__(self):
        self.items: List[T] = []

    def add_item(self, item: T):
        self.items.append(item)

    def get_items(self) -> List[T]:
        return self.items

    def check_type(self):
        if self.items:
            return type(self.items[0])
        else:
            return None

# Test the GenericList class with different data types


# Create a GenericList for integers
int_list = GenericList()
int_list.add_item(1)
int_list.add_item(2)
int_list.add_item(3)
print("Integer List:", int_list.get_items())
print("Type of items in Integer List:", int_list.check_type())

# Create a GenericList for strings
str_list = GenericList()
str_list.add_item("apple")
str_list.add_item("banana")
str_list.add_item("orange")
print("String List:", str_list.get_items())
print("Type of items in String List:", str_list.check_type())
