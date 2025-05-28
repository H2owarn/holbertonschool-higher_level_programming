#!/usr/bin/env python3
"""This module create an abstract class named Shape
 with two abstract methods: area and perimeter."""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

 # Subclass implementing the blueprint

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * abs(self.radius)  # Convert to positive

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(Shape):
    print ("Area: {}".format(Shape.area()))
    print ("Perimeter:: {}".format(Shape.perimeter()))
