sentence = input("Please type in a sentence:")
words = sentence.split()
index = 0

while index < len(words):
    print(words[index][0])  # print the first letter of the current word
    index += 1