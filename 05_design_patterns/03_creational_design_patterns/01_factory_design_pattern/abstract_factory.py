from abc import ABC, abstractmethod

class Obstacle(ABC):
    @abstractmethod
    def action(self) -> str:
        pass

class Frog:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle: "Obstacle") -> None:
        act = obstacle.action()
        msg = f"{self} the Frog encounters {obstacle} and {act}!"
        print(msg)

class Bug:
    def __str__(self) -> str:
        return "a bug"

    def action(self) -> str:
        return "eats it"


class Wizard:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle: "Obstacle") -> None:
        act = obstacle.action()
        msg = f"{self} the Wizard battles against {obstacle} and {act}!"
        print(msg)

class Ork:
    def __str__(self) -> str:
        return "an evil ork"

    def action(self) -> str:
        return "kills it"


class FrogWorld:
    def __init__(self, name: str):
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return "\n\n\t------ Frog World -------"

    def make_character(self) -> Frog:
        return Frog(self.player_name)

    def make_obstacle(self) -> Bug:
        return Bug()

class WizardWorld:
    def __init__(self, name: str):
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return "\n\n\t------ Wizard World -------"

    def make_character(self) -> Wizard:
        return Wizard(self.player_name)

    def make_obstacle(self) -> Ork:
        return Ork()



# Game Environment
class GameEnvironment:
    def __init__(self, factory: object):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self) -> None:
        self.hero.interact_with(self.obstacle)


def validate_age(name: str) -> tuple[bool, int]:
    age = None
    try:
        age_input = input(f"Welcome {name}. How old are you? ")
        age = int(age_input)
    except ValueError:
        print(f"Age {age_input} is invalid, please try again...")
        return False, age
    return True, age

def main() -> None:
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(factory=game(name))
    environment.play()

if __name__ == "__main__":
    main()