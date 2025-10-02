# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for row in range(row_no, row_no + 3):
        for col in range(column_no, column_no + 3):
            value = sudoku[row][col]
            if value != 0:
                if value in numbers:
                    return False
                numbers.append(value)
    return True