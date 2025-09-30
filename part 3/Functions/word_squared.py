def squared(word, size):
    counter = 0
    row = 0
    while row < size:
        line = ""
        col = 0
        while col < size:
            line += word[counter % len(word)]
            counter += 1
            col += 1
        print(line)
        row += 1


# model solution
def squared2(characters, size):
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += characters[i % len(characters)]
        i += 1
    print(row)