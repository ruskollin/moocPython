# Write your solution here
def everything_reversed(strings):
    newList = []
    for string in strings[::-1]:
        reversedString = string[::-1]
        newList.append(reversedString)
    return newList