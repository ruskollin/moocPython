# Write your solution here
def dict_of_numbers():
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    numbers_dict = {}

    for i in range(0, 100):
        if i <= 9:
            numbers_dict[i] = ones[i]
        elif i <= 19:
            numbers_dict[i] = teens[i - 10]
        else:
            ten_part = i // 10
            one_part = i % 10
            if one_part == 0:
                numbers_dict[i] = tens[ten_part]
            else:
                numbers_dict[i] = tens[ten_part] + "-" + ones[one_part]

    return numbers_dict
