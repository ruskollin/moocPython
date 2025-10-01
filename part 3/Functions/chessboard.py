def chessboard(size):
    row = 0
    while row < size:
        line = ""
        col = 0
        while col < size:
            if (row + col) % 2 == 0:
                line += "1"
            else:
                line += "0"
            col += 1
        print(line)
        row += 1
