print("Please type in integer numbers. Type in 0 to finish.")
number = int(input("Number: "))
count = 0
total = 0
positives = 0
negatives = 0

while number != 0:
    count += 1
    total += number
    
    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1

    number = int(input("Number: "))

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {total / count}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")