from typing import Generic, TypeVar, List

T = TypeVar('T')  # Type variable for elements in the container

class Container(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def get_all(self) -> List[T]:
        return self._items

# Subclass inheriting from Container
class StringContainer(Container[str]):
    def __init__(self) -> None:
        super().__init__()  # Call the constructor of the base class
    
    def join_strings(self, delimiter: str = ' ') -> str:
        return delimiter.join(self.get_all())

# Example usage
if __name__ == "__main__":
    string_container = StringContainer()
    string_container.add("Hello")
    string_container.add("World")
    string_container.add("!")

    print(string_container.join_strings())  # Output: Hello World !
