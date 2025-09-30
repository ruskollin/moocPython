limit = int(input("Limit: "))

total = 0
number = 1
result = ""

while total < limit:
    total += number
    if result == "":
        result = str(number)
    else:
        result += " + " + str(number)
    number += 1

print(f"The consecutive sum: {result} = {total}")