class ExceptionsDemo:
    @staticmethod
    def show():
        try:
            with open("file.txt") as reader:
                if reader:
                    print("File opened")
        except FileNotFoundError as e:
            print("File not found")
            print(e)


ExceptionsDemo.show()
