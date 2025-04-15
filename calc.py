# Simple Calculator Program

# Ask user for the first number
num1 = float(input("Enter the first number: "))

# Ask user for the second number
num2 = float(input("Enter the second number: "))

# Ask user for the operation
operation = input("Enter an operation (+, -, *, /): ")

# Perform the chosen operation
#addition operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
#negative operation
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
#multiplication operation
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
#division operation
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
