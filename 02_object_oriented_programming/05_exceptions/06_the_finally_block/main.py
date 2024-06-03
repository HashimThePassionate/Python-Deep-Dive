class ExceptionsDemo:
    @staticmethod
    def show():
        reader = None
        try:
            reader = open("file.txt", "r")
            value = reader.read()
            # This line prints the read content for demonstration purposes
            print(value)
        except IOError as e:
            print("Could not read data")
        finally:
            if reader is not None:
                try:
                    reader.close()
                except IOError as e:
                    print("Could not close the file")
                    print(e)


ExceptionsDemo.show()
