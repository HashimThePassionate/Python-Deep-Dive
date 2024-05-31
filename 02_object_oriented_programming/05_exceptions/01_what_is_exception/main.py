class ExceptionsDemo:
    @staticmethod
    def show():
        ExceptionsDemo.say_hello(None)

    @staticmethod
    def say_hello(name):
        print(name.upper())


ExceptionsDemo.show()
