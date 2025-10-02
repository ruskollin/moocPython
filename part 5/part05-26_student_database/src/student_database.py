# Write your solution here
def add_student(students: dict, name: str):
    if name not in students:
        students[name] = {}

def add_course(students: dict, name: str, course: tuple):
    if name not in students:
        return
    course_name, grade = course
    if grade == 0:
        return
    if course_name not in students[name] or grade > students[name][course_name]:
        students[name][course_name] = grade

def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return
    courses = students[name]
    if not courses:
        print(f"{name}:\n no completed courses")
        return
    num_courses = len(courses)
    print(f"{name}: {num_courses} completed courses:")
    for course_name, grade in courses.items():
        print(f" {course_name} {grade}")
    avg = sum(courses.values()) / num_courses
    print(f" average grade {avg:.1f}")

def summary(students: dict):
    num_students = len(students)
    most_courses = -1
    best_avg = -1
    student_most_courses = ""
    student_best_avg = ""
    for name, courses in students.items():
        num_courses = len(courses)
        if num_courses > most_courses:
            most_courses = num_courses
            student_most_courses = name
        if num_courses > 0:
            avg = sum(courses.values()) / num_courses
            if avg > best_avg:
                best_avg = avg
                student_best_avg = name
    print(f"students {num_students}")
    print(f"most courses completed {most_courses} {student_most_courses}")
    print(f"best average grade {best_avg:.1f} {student_best_avg}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    summary(students)