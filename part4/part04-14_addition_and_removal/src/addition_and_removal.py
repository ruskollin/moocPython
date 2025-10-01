# Write your solution here
numbers = []
print(f"The list is now {numbers}")

while True:
    choice = input("a(d)d, (r)emove or e(x)it: ")

    if choice == "r":
        numbers.pop()
        print(f"The list is now {numbers}")

    elif choice == "d":
        if len(numbers) == 0:
            numbers.append(1)
        else:
            numbers.append(numbers[-1] + 1)
        print(f"The list is now {numbers}")

    elif choice == "x":
        print("Bye!")
        break
