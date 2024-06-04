from typing import Dict, Generic, TypeVar

T = TypeVar("T")

class Registry(Generic[T]):
    def __init__(self) -> None:
        self._store: Dict[str, T] = {}
          
    def set_item(self, k: str, v: T) -> None:
        self._store[k] = v
    
    def get_item(self, k: str) -> T:
        return self._store[k]
  
family_name_reg = Registry[str]()
family_age_reg = Registry[int]()

family_name_reg.set_item("husband", "steve")
print(family_name_reg.get_item('husband'))
print(type(family_name_reg.get_item('husband')))
family_name_reg.set_item("dad", "john")

family_age_reg.set_item("steve", 30)
print(family_age_reg.get_item('steve'))
print(type(family_age_reg.get_item('steve')))