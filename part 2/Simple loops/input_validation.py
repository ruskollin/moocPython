from math import sqrt

while True:
    number = int(input("Please type in a number: "))
    
    if number == 0:
        print("Exiting...")
        break
    elif number < 0:
        print("Invalid number")
    else:
        print(sqrt(number))