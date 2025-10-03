# Write your solution here
def no_vowels(s: str):
    vowels = "aeiou"
    result = ""

    for char in s:
        if char not in vowels:
            result += char
    return result
