# Write your solution here
def line(num, word):
    char = "*"
    if word != "":
        char = word[0]
    print(char * num)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")