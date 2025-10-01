word = input("Please type in a word: ")
char = input("Please type in a character: ")
index = 0

while index < len(word):
    if word[index] == char:
        if index + 2 < len(word):
            print(word[index:index+3])
    index += 1
