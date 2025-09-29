name = input("Please tell me your name:")

if name == "Jerry":
    print("Next please!")
else:
    portions = int(input("How many portions of soup?"))
    cost = portions * 5.90

    print(f"The total cost is {cost:.2f}")
    print("Next please!")