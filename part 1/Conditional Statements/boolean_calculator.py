number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
operation = input("Operation:")

if operation == "add":
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operation == "multiply":
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == "subtract":
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")