word = input("Word: ")
frame_width = 30
spaces = frame_width - 2 - len(word)

left_spaces = spaces // 2
right_spaces = spaces - left_spaces

print("*" * frame_width)
print("*" + " " * left_spaces + word + " " * right_spaces + "*")
print("*" * frame_width)
