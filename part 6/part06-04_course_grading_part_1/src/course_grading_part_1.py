# Write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students = {}
with open(student_info) as file:
    first_line = True
    for line in file:
        line = line.replace("\n", "")
        if first_line:
            first_line = False
            continue
        parts = line.split(";")
        id = parts[0]
        first = parts[1]
        last = parts[2]
        students[id] = f"{first} {last}"

exercises = {}
with open(exercise_data) as file:
    first_line = True
    for line in file:
        line = line.replace("\n", "")
        if first_line:
            first_line = False
            continue
        parts = line.split(";")
        id = parts[0]
        total = 0
        for num in parts[1:]:
            total += int(num)
        exercises[id] = total

for id, name in students.items():
    if id in exercises:
        print(f"{name} {exercises[id]}")