# Write your solution here
def all_the_longest(strings):
    longest_length = 0
    for string in strings:
        if len(string) > longest_length:
            longest_length = len(string)

    longest_strings = []
    for string in strings:
        if len(string) == longest_length:
            longest_strings.append(string)

    return longest_strings

