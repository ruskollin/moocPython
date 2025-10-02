# Write your solution here
def invert(dictionary: dict):
    original_items = list(dictionary.items())
    dictionary.clear()
    
    for key, value in original_items:
        dictionary[value] = key