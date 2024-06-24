import collections
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]



beer_card = Card('7', 'diamonds')
print(beer_card)  # Output: Card(rank='7', suit='diamonds')
deck = FrenchDeck()
print(len(deck))  # Output: 52
print(deck[0])   # Output: Card(rank='2', suit='spades')
print(deck[-1])  # Output: Card(rank='A', suit='hearts')
print(choice(deck))  # Example output: Card(rank='3', suit='hearts')
print(deck[:3])       # Output: [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
print(deck[12::13])   # Output: [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
for card in deck:
    print(card)
print(Card('Q', 'hearts') in deck)  # Output: True
