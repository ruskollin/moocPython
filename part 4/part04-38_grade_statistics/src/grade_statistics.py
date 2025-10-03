# Write your solution here
results = []

while True:
    line = input("Exam points and exercises completed: ")
    if line == "":
        break
    parts = line.split()
    examPoints = int(parts[0])
    exercises = int(parts[1])

    results.append((examPoints, exercises))

print("Statistics:")

if len(results) == 0:
    print("No data available.")
else:
    totalPoints = 0
    passedCount = 0

    grades = [0, 0, 0, 0, 0, 0]

    for examPoints, exercises in results:
        exercisePoints = exercises // 10

        if examPoints < 10:
            grade = 0
        else:
            total = examPoints + exercisePoints

            if total <= 14:
                grade = 0
            elif total <= 17:
                grade = 1
            elif total <= 20:
                grade = 2
            elif total <= 23:
                grade = 3
            elif total <= 27:
                grade = 4
            else:
                grade = 5

        grades[grade] += 1
        totalPoints += examPoints + exercisePoints
        if grade > 0:
            passedCount += 1

    averagePoints = totalPoints / len(results)
    passPercentage = (passedCount / len(results)) * 100

    print(f"Points average: {averagePoints:.1f}")
    print(f"Pass percentage: {passPercentage:.1f}")
    print("Grade distribution:")

    for grade in range(5, -1, -1):
        print(f"  {grade}: {'*' * grades[grade]}")