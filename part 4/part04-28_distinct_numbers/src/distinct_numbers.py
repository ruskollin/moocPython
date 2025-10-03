# Write your solution here
def distinct_numbers(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    unique.sort()
    return unique