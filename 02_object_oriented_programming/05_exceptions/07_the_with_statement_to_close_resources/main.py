class ExceptionsDemo:
    @staticmethod
    def show():
        reader = None
        try:
            reader = open("file.txt", "r")
            with reader:
                value = reader.read()
                print(value)  # This line prints the read content for demonstration purposes
                print("The 'with' statement automatically closed the file.")
        except FileNotFoundError:
            print("File not found.")
        except IOError as e:
            print("Could not read data")
            print(e)
        finally:
            if reader is not None:
                if not reader.closed:
                    reader.close()
                    print("File closed manually.")
                else:
                    print("File was already closed by 'with' statement.")

# Call the show method to demonstrate
ExceptionsDemo.show()
