# Write your solution here
def longest(strings: list):
    longestString = strings[0]
    for string in strings:
        if len(string) > len(longestString):
            longestString = string
    return longestString


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))