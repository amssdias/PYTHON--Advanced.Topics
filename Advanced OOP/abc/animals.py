from abc import ABCMeta, abstractmethod

# Abstract Base Class
class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking...')

    # We no longer want to interact directly with Animal Class
    # Whenever I have a subclass of type animal, this method will be available
    @abstractmethod
    def num_legs(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name
    
    def num_legs(self):
        return 2

animals = [Dog('roldf'), Monkey('Bob')]

for a in animals:
    print(a.num_legs())