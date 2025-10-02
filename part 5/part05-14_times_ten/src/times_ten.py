# Write your solution here
def times_ten(start_index: int, end_index: int):
    lists = {}
    while start_index <= end_index:
        lists[start_index] = start_index * 10
        start_index += 1
    return lists

if __name__ == "__main__":
    times_ten(3,6)
