def safe_calculator():    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation: ")
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else:
            print("Invalid operation!")
            return
            
        print(f"Result: {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero")

safe_calculator()