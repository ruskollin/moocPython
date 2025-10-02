# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_grid = []
    for i in range(9):
        new_row = []
        for j in range(9):
            new_row.append(sudoku[i][j])
        new_grid.append(new_row)
    new_grid[row_no][column_no] = number
    return new_grid

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