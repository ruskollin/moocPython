# Write your solution here
def shortest(strings):
    shortest_string = strings[0]
    for string in strings:
        if len(string) < len(shortest_string):
            shortest_string = string

    return shortest_string