def add(x, y):
    print(x + y)

def subtract(x, y):
    print(x - y)

def multiply(x, y):
    print(x * y)

def divide(x, y):
    try:
        print(x / y)
    except ZeroDivisionError:
        print("Cannot divide by zero")