Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #classes
>>> class Car():
...     def __init__(self, brand, year):
...         self.brand = brand
...         self.year = year
... 
...         
>>> c1 = Car('Toyota', 2026)
>>> print(c1.brand, c1.year)
Toyota 2026
