class Console:
    @staticmethod
    def read_number(prompt, min_value, max_value):
        while True:
            try:
                value = float(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"Enter a value between {min_value} and {max_value}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Example usage:
# console = Console()
# number = console.read_number("Enter a number: ", 0, 100)
# print("Entered number:", number)
# print(Console.read_number('Enter a Number: ',0,10))
