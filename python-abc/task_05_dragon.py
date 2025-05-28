#!/usr/bin/env python3
"""This module Design two mixin classes, SwimMixin and FlyMixin"""


class SwimMixin:
    """Design a mixin called SwimMixin."""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Design a mixin called FlyMixin."""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


draco = Dragon()
