from abc import ABCMeta, abstractmethod

class MyABC(metaclass=ABCMeta):
    @abstractmethod
    def my_abstract_method(self):
        pass


my = MyABC()  # TypeError: Can't instantiate abstract class MyABC with abstract methods