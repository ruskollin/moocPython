# Write your solution here
def runNegToPos():
    number = int(input("Please type in a positive integer: "))

    for num in range(-number, number + 1):
        if num != 0:
            print(num)

runNegToPos()