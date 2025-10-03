# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

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

exams = {}
with open(exam_data) as file:
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
        exams[id] = total

for id, name in students.items():
    if id in exercises and id in exams:
        exercise_total = exercises[id]
        exercise_points = (exercise_total * 10) // 40

        exam_points = exams[id]
        total_points = exercise_points + exam_points

        if total_points <= 14:
            grade = 0
        elif total_points <= 17:
            grade = 1
        elif total_points <= 20:
            grade = 2
        elif total_points <= 23:
            grade = 3
        elif total_points <= 27:
            grade = 4
        else:
            grade = 5

        print(f"{name} {grade}")