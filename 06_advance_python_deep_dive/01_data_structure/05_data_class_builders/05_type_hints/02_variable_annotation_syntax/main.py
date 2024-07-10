from typing import NamedTuple, List, Tuple,  Optional

class FrenchDeck:
    def __init__(self):
        self.cards = ["Ace of Spades", "2 of Hearts", "3 of Clubs", "4 of Diamonds"]
    
    def __repr__(self):
        return f"FrenchDeck(cards={self.cards})"

class Card(NamedTuple):
    name: str
    deck: FrenchDeck

# Creating an instance
deck = FrenchDeck()
card = Card(name="Ace of Spades", deck=deck)
print(card)

# NamedTuple with multiple fields
class Point(NamedTuple):
    coordinates: Tuple[str, float]
    values: List[int]

# Creating an instance
point = Point(coordinates=("latitude", 42.0), values=[1, 2, 3, 4])
print(point)



class User(NamedTuple):
    nickname: Optional[str]

# Creating instances
user_with_nickname = User(nickname="Hashim")
user_without_nickname = User(nickname=None)
print(user_with_nickname)
print(user_without_nickname)

