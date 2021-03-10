from database import Database
from abc import ABCMeta, abstractmethod

class Saveable(metaclass=ABCMeta):
    def save(self):
        Database.insert(self.to_dict)

    # This would be an interface because defines the functionality that should be in a subclass
    @abstractmethod
    def to_dict(self):
        pass