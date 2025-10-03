# Copy here code of line function from previous exercise and use it in your solution
def line(num, word):
    char = "*"
    if word != "":
        char = word[0]
    print(char * num)

def shape(triangleSize, triangleChar, rectHeight, rectChar):
    row = 1
    while row <= triangleSize:
        line(row, triangleChar)
        row = row + 1

    rectRow = 0
    while rectRow < rectHeight:
        line(triangleSize, rectChar)
        rectRow = rectRow + 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")