from typing import Generic, TypeVar, Dict

K = TypeVar('K')  # Key type
V = TypeVar('V')  # Value type

class GenericDict(Generic[K, V]):
    def __init__(self) -> None:
        self._store: Dict[K, V] = {}
          
    def set_item(self, key: K, value: V) -> None:
        self._store[key] = value
    
    def get_item(self, key: K) -> V:
        return self._store[key]
    
    def __str__(self) -> str:
        items = [f"{key} = '{value}'" for key, value in self._store.items()]
        return ", ".join(items)
    
# Example usage
if __name__ == "__main__":
    str_int_dict = GenericDict[str, int]()
    str_int_dict.set_item("one", 1)
    str_int_dict.set_item("two", 2)
    
    print(str_int_dict)  # Output: one = '1', two = '2'

    int_str_dict = GenericDict[int, str]()
    int_str_dict.set_item('name', "Muhammad Hashim")
    int_str_dict.set_item('age', "24")
    
    print(int_str_dict)  # Output: 1 = 'one', 2 = 'two'
