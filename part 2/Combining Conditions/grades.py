points = int(input("How many points [0-100]: "))

if points < 0 or points > 100:
    print("Grade: impossible!")
elif points <= 49:
    print("Grade: fail")
elif points <= 59:
    print("Grade: 1")
elif points <= 69:
    print("Grade: 2")
elif points <= 79:
    print("Grade: 3")
elif points <= 89:
    print("Grade: 4")
else:
    print("Grade: 5")