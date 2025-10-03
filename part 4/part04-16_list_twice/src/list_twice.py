# Write your solution here
items = []

while True:
    newItem = int(input("New item: "))
    
    if newItem == 0:
        print("Bye!")
        break

    items.append(newItem)
    print(f"The list now: {items}")

    sortedItems = sorted(items)
    print(f"The list in order: {sortedItems}")
