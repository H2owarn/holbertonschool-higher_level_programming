#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)



try:
    bg.integer_validator("age", True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

