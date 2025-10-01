# Write your solution here
def palindromes(word):
    letters = list(word)
    letters.reverse()
    reversedWord = "".join(letters) 
    return word == reversedWord

while True:
    userInput = input("Please type in a palindrome: ")
    if palindromes(userInput):
        print(f"{userInput} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
