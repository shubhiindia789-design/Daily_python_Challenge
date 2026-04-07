Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
def calculator():
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    op = input("Enter operation(+,-,*,/):")

    if op == "+":
...         print("Result:" , a+b)
... 
...     elif op == "-":
...         print("Result:" , a-b)
... 
...     elif op == "*":
...         print("Result:" , a*b)
... 
...     elif op == "/":
...         try:
...             print("Result:" , a/b)
...         except ZeroDivisionError:    
...                 print("Cannot divide by zero!")
... 
...     else:
...         print("Invalid operation")
... 
...     calculator()
... 
...     
>>> 7+8
15
>>> 9-6
3
>>> 6*3
18
>>> 9/3
3.0
>>> 5/0
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    5/0
ZeroDivisionError: division by zero
>>> 0/5
0.0
>>> 5//8
0
>>> 6&5
4
