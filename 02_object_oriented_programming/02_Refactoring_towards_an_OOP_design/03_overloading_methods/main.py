class Console:
    @staticmethod
    def read_number(prompt, min_value=None, max_value=None):
        while True:
            try:
                value = float(input(prompt))
                if min_value is not None and max_value is not None:
                    if min_value <= value <= max_value:
                        return value
                    else:
                        print(f"Enter a value between {
                              min_value} and {max_value}")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
