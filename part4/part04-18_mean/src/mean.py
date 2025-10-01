# Write your solution here
def mean(numbers: list):
    index = 0
    total = 0
    count = 0
    while index < len(numbers):
        total += numbers[index]
        count += 1
        index += 1
    if count == 0:
        return 0
    return total / count

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)