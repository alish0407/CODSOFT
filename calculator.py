import math

# Define a function for each operation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def modulus(x, y):
    return x % y

def exponent(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Invalid input for square root"
    return math.sqrt(x)

# Main function to take user input and perform calculations

def calculator():
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'modulus' for modulus")
    print("Enter 'exponent' for exponentiation")
    print("Enter 'square_root' for square root")
    print("Enter 'exit' to end the program")
    
    while True:
        choice = input("Enter your choice: ")
        
        if choice == "exit":
            break
        
        if choice in ("add", "subtract", "multiply", "divide", "modulus", "exponent", "square_root"):
            if choice == "square_root":
                num = float(input("Enter the number: "))
                result = square_root(num)
            else:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                if choice == "add":
                    result = add(num1, num2)
                elif choice == "subtract":
                    result = subtract(num1, num2)
                elif choice == "multiply":
                    result = multiply(num1, num2)
                elif choice == "divide":
                    result = divide(num1, num2)
                elif choice == "modulus":
                    result = modulus(num1, num2)
                elif choice == "exponent":
                    result = exponent(num1, num2)
                
            print("Result: ", result)
        else:
            print("Invalid input. Please try again.")

calculator()
