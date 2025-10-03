# Write your solution here
def most_common_character(word):
    maxCount = 0
    mostCommon = ""

    for char in word:
        count = word.count(char)
        if count > maxCount:
            maxCount = count
            mostCommon = char
    return mostCommon