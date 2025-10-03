# Copy here code of line function from previous exercise
def line(num, word):
    char = "*"
    if word != "":
        char = word[0]
    print(char * num)

def square_of_hashes(height):
    # You should call function line here with proper parameters
    row = 0
    while row < height:
        line(height, "#")
        row = row + 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
