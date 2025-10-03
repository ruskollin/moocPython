# Write your solution here
def no_shouting(strings):
    result = []
    for string in strings:
        if not string.isupper():
            result.append(string)
    return result
