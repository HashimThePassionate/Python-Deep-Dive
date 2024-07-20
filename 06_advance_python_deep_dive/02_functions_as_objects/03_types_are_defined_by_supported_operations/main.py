# from collections import abc

# def double(x: abc.Sequence):
#     return x * 2





# from typing import List, TypeVar, Generic

# T = TypeVar('T')

# class CustomSequence(Generic[T]):
#     def __init__(self, items: List[T]):
#         self.items = items

#     def __getitem__(self, index: int) -> T:
#         return self.items[index]

#     def __len__(self) -> int:
#         return len(self.items)

#     def __mul__(self, other: int) -> 'CustomSequence[T]':
#         if isinstance(other, int):
#             return CustomSequence(self.items * other)
#         else:
#             return NotImplemented

# def double(x: CustomSequence[T]) -> CustomSequence[T]:
#     return x * 2

# # Testing the double function with CustomSequence
# seq = CustomSequence([1.0, 2.0, 3.0])
# result = double(seq)
# print(result.items)  # Output: [1, 2, 3, 1, 2, 3]


class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print('Quack!')

def alert(birdie):
    birdie.quack()

def alert_duck(birdie: Duck) -> None:
    birdie.quack()

def alert_bird(birdie: Bird) -> None:
    birdie.quack()
