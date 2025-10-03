# Write your solution here
def read_input(prompt, low, high):
    while True:
        try:
            number = int(input(prompt))
            if number >= low and number <= high:
                return number
            else:
                print(f"You must type in an integer between {low} and {high}")
        except ValueError:
            print(f"You must type in an integer between {low} and {high}")