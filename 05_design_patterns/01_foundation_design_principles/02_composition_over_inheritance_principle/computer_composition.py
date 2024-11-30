class CPU:
    def process(self) -> None:
        print("CPU is processing data.")

class RAM:
    def load_data(self) -> None:
        print("RAM is loading data.")

class Storage:
    def read_data(self) -> None:
        print("Storage is reading data.")

class Computer:
    def __init__(self) -> None:
        self.cpu: CPU = CPU()
        self.ram: RAM = RAM()
        self.storage: Storage = Storage()
    
    def start(self) -> None:
        self.cpu.process()
        self.ram.load_data()
        self.storage.read_data()
        print("Computer has started successfully!")

if __name__ == "__main__":
    my_computer: Computer = Computer()
    my_computer.start()