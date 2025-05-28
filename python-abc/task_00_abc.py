#!/usr/bin/env python3
"""This module create an abstract class"""


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Return dog sound"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Return cat sound"""
    def sound(self):
        return "Meow"
