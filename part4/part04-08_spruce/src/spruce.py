# Write your solution here
def line(num, word):
    char = "*"
    if word != "":
        char = word[0]
    print(char * num)
    
def spruce(size):
    print("a spruce!")
    row = 1

    while row <= size:
        stars = 2 * row - 1
        spaces = size - row
        print(" " * spaces, end="")
        line(stars, "*")
        row = row + 1

    print(" " * (size - 1), end="")
    line(1, "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)