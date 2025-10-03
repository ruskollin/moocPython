# Write your solution here
def sum_of_positives(numbers: list):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total
