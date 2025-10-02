# Write your solution here
def print_sudoku(sudoku: list):
    row_index = 0
    for row in sudoku:
        col_index = 0
        for value in row:
            if value != 0:
                print(value, end=" ")
            else:
                print("_", end=" ")
            if (col_index + 1) % 3 == 0 and col_index != 8:
                print(" ", end="")
            col_index += 1
        print()

        if (row_index + 1) % 3 == 0 and row_index != 8:
            print()
        row_index += 1

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)

    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)