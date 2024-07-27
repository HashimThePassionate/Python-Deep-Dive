import random
from typing import List
from datetime import date, timedelta


class BirthdayParadox:
    def __init__(self, num_birthdays: int = 23, num_simulations: int = 100_000) -> None:
        self.num_birthdays: int = num_birthdays
        self.num_simulations: int = num_simulations

    def _generate_birthdays(self) -> List[str]:
        """Generate a list of random birthdays."""
        birthdays = []
        for _ in range(self.num_birthdays):
            start_of_year = date(2024, 1, 1)
            random_number_of_days = timedelta(random.randint(0, 364))
            birthday = start_of_year + random_number_of_days
            birthdays.append(birthday.strftime('%b %d'))
        return birthdays

    def _has_duplicate(self, birthdays: List[str]) -> bool:
        """Check if there are any duplicate birthdays in the list."""
        return len(birthdays) != len(set(birthdays))

    def __call__(self) -> None:
        print("\n\nBirthday Paradox, by Hashim")
        print(f"How many birthdays shall I generate? (Max 100)")
        num_birthdays = int(input("> "))
        self.num_birthdays = min(num_birthdays, 100)
        birthdays = self._generate_birthdays()
        print(f"\nHere are {self.num_birthdays} birthdays:")
        for birthday in birthdays:
            print(birthday, end=', ')
        print("\n")
        if self._has_duplicate(birthdays):
            print(
                "In this simulation, multiple people have a birthday on the same date.\n")
        else:
            print("In this simulation, all birthdays are unique.\n")
        print(f"Generating {self.num_birthdays} random birthdays {
              self.num_simulations} times...")
        input("Press Enter to begin...\n")
        self.simulate()

    def simulate(self) -> None:
        """Run the birthday simulation."""
        match_count = 0
        for i in range(self.num_simulations):
            if self._has_duplicate(self._generate_birthdays()):
                match_count += 1
            if (i + 1) % 10000 == 0:
                print(f"{i + 1} simulations run...")
        probability = match_count / self.num_simulations * 100
        print(f"Out of {self.num_simulations} simulations of {
              self.num_birthdays} people, there was a")
        print(f"matching birthday in that group {
              match_count} times. This means")
        print(f"that {self.num_birthdays} people have a {
              probability:.2f}% chance of")
        print("having a matching birthday in their group.")
        print("That's probably more than you would think!")


experiment = BirthdayParadox()
experiment()
