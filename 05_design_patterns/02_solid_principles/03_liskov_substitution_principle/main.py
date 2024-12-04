class Bird:
    def move(self) -> None:
        print("I'm moving")

class FlyingBird(Bird):
    def move(self) -> None:
        print("I'm flying")

class FlightlessBird(Bird):
    def move(self) -> None:
        print("I'm walking")

def make_bird_move(bird: Bird) -> None:
    bird.move()

if __name__ == "__main__":
    generic_bird: Bird = Bird()
    eagle: FlyingBird = FlyingBird()
    penguin: FlightlessBird = FlightlessBird()

    make_bird_move(generic_bird)  # Output: I'm moving
    make_bird_move(eagle)         # Output: I'm flying
    make_bird_move(penguin)       # Output: I'm walking
