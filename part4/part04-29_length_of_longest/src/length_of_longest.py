# Write your solution here
def length_of_longest(strings):
    longest_length = 0
    for string in strings:
        if len(string) > longest_length: 
            longest_length = len(string)

    return longest_length