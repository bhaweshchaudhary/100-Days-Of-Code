student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grade = {

}

# TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grade[student] = "Outstanding"
    elif score > 80:
        student_grade[student] = "Exceeds Expectations"
    elif score > 70:
        student_grade[student] = "Acceptable"
    else:
        student_grade[student] = "Fail"
# 🚨 Don't change the code below 👇
print(student_grade)
