# Write your solution here
def histogram(text: str):
    counts = {}
    for char in text:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    
    for char, count in counts.items():
        print(char, "*" * count)

if __name__ == "__main__":
    histogram("abba")