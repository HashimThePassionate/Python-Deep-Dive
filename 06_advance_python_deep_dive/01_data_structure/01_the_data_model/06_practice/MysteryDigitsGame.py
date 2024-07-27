import random
# import inspect


# def internal_only(method):
#     def wrapper(*args, **kwargs):
#         caller = inspect.stack()[1].function
#         if caller not in ['__init__', 'play_game', 'reset_game']:
#             raise PermissionError(f"Error: Method '{
#                                   method.__name__}' is restricted and cannot be accessed directly.")
#         return method(*args, **kwargs)
#     return wrapper


class MysteryDigitsGame:
    def __init__(self) -> None:
        self.secret_number: str = self._generate_secret_number()
        self.guesses: int = 10

    # @internal_only
    def _generate_secret_number(self) -> str:
        """Generate a random 3-digit number with unique digits."""
        digits = list('0123456789')
        random.shuffle(digits)
        return ''.join(digits[:3])

    def __str__(self) -> str:
        return "MysteryDigits, a deductive logic game by Hashim.\nI am thinking of a 3-digit number. Try to guess what it is."

    def __call__(self) -> None:
        print(self)
        print("Here are some clues:\nWhen I say: That means:\n Pico One digit is correct but in the wrong position.\n Fermi One digit is correct and in the right position.\n Bagels No digit is correct.")
        print("I have thought up a number. You have 10 guesses to get it.")
        self.play_game()

    # @internal_only
    def _get_clues(self, guess: str) -> str:
        """Provide clues based on the guess."""
        if guess == self.secret_number:
            return "You got it!"

        clues = []
        for i in range(len(guess)):
            if guess[i] == self.secret_number[i]:
                clues.append("Fermi")
            elif guess[i] in self.secret_number:
                clues.append("Pico")
        if not clues:
            return "Bagels"
        return ' '.join(clues)

    def play_game(self) -> None:
        """Main game loop."""
        for guess_num in range(1, self.guesses + 1):
            guess: str = ''
            while len(guess) != 3 or not guess.isdigit():
                guess = input(f"Guess #{guess_num}: ")

            clues = self._get_clues(guess)
            print(clues)
            if clues == "You got it!":
                break
        else:
            print(f"Sorry, you've run out of guesses. The number was {
                  self.secret_number}")

        if input("Do you want to play again? (yes or no) ").lower().startswith('y'):
            self.reset_game()
            self.play_game()

    def reset_game(self) -> None:
        self.secret_number = self._generate_secret_number()
        self.guesses = 10


game = MysteryDigitsGame()
game()


# game = MysteryDigitsGame()
# try:
#     game._generate_secret_number()
# except PermissionError as e:
#     print(e)
# game = MysteryDigitsGame()
# try:
#     game._get_clues('123')
# except PermissionError as e:
# print(e)
