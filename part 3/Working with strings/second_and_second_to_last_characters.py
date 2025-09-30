text = input("Please type in a string: ")

second = text[1]         # second character
second_to_last = text[-2]  # second to last character

if second == second_to_last:
    print(f"The second and the second to last characters are {second}")
else:
    print("The second and the second to last characters are different")