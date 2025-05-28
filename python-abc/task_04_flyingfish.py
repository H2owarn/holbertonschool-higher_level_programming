#!/usr/bin/env python3
"""This module Create a FlyingFish class that inherits
 from both a Fish class and a Bird class."""

class Fish:
    """Create Fish class"""
    def swim(self):
        return("The fish is swimming")
    def habitat(self):
        return("The fish lives in water")

class Bird:
    """Create Bird class"""
    def fly(self):
        return("The flying fish is soaring!")
    def habitat(self):
        return("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """FlyuingFish inherits from both Fish and Bird"""
    def swim(self):
        print("The flying fish is swimming!")
        super().swim()
    def fly(self):
        print("The flying fish is soaring!")
        super().fly()
    def habitat(self):
        print("The flying fish lives both in water and the sky!")
        super().habitat()
