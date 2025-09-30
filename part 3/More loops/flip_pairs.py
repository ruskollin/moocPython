number = int(input("Please type in a number: "))

i = 1
while i <= number:
    if i + 1 <= number:
        print(i + 1)
        print(i)
        i += 2 
    else:
        print(i)
        i += 1
