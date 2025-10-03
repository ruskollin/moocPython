# Write your solution here
def same_chars(word, x, y):
    if x < 0 or x >= len(word):
        return False

    if y < 0 or y >= len(word):
        return False

    if word[x] == word[y]:
        return True
    else:
        return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))