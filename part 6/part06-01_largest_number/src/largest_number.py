# write your solution here
def largest():
    with open("numbers.txt") as f:
        max_num = None
        for line in f:
            num = int(line)
            if max_num is None or num > max_num:
                max_num = num
    return max_num

