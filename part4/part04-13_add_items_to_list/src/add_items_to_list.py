# Write your solution here
count = int(input("How many items:"))
items = []

i = 1
while i <= count:
    value = int(input(f"Item {i}: "))
    items.append(value)
    i = i + 1

print(items)