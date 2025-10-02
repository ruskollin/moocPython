# Write your solution here
def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        value = row[column_no]
        if value != 0:
            if value in numbers:
                return False
            numbers.append(value)
    return True