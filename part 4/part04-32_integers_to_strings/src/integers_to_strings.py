# Write your solution here
def formatted(numbers: list):
    new_list = []
    for num in numbers:
        formatted_num = f"{num:.2f}"
        new_list.append(formatted_num)
    return new_list