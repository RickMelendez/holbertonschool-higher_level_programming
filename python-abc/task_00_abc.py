#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class
    Defines the blueprint for animal classes with an abstract method 'sound'.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        Should return the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Subclass of Animal representing a Dog.
    Implements the sound method to return "Bark".
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal representing a Cat.
    Implements the sound method to return "Meow".
    """

    def sound(self):
        return "Meow"


dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())
