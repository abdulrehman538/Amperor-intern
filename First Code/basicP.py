def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


def show_student(name, marks):
    result = check_result(marks)
    print("Name:", name)
    print("Marks:", marks)
    print("Result:", result)
    print("-------------------")


def main():
    students = [
        ("Ali", 75),
        ("Ahmed", 35),
        ("Sara", 90),
        ("John", 40)
    ]

    for student in students:
        name = student[0]
        marks = student[1]
        show_student(name, marks)


main()