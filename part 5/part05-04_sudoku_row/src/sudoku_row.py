# Write your solution here
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for value in sudoku[row_no]:
        if value != 0:
            if value in numbers:
                return False
            numbers.append(value)
    return True