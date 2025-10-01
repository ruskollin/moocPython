# Write your solution here
def longest_series_of_neighbours(numbers):
    maxLength = 1
    currentLength = 1

    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i-1]) == 1:
            currentLength += 1
        else:
            currentLength = 1
        if currentLength > maxLength:
            maxLength = currentLength

    return maxLength