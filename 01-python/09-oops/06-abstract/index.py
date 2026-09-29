# Abstract Base Class (ABC) is used to achieve data abstraction by defining a common interface for its subclasses. It cannot be instantiated directly and serves as a blueprint for other classes.

# Abstract classes are created using abc module and @abstractmethod decorator, allowing developers to enforce method implementation in subclasses while hiding complex internal logic.

from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())