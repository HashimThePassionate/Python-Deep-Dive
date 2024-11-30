class Engine:
    def start(self) -> None:
        print("Engine started")

class Car:
    def __init__(self) -> None:
        self.engine: Engine = Engine()
    
    def start(self) -> None:
        self.engine.start()
        print("Car started")
        
if __name__ == "__main__":
    my_car: Car = Car()
    my_car.start()
