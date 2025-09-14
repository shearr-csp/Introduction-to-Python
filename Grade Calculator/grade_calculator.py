# Initialize Data
student_grades = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [],
    "David": [65, 70, 68],
    "Esther": [100, 100, 100],
}
print("Student Grades:")
print(student_grades)
print(" ")

# 1 Calculate Average Grades
student_averages = {}
for student, grades in student_grades.items():
    # Calculate the average manually by summing the grades and dividing by the count
    # Checks to see if there are any grades in the student_grades dictionary
    if len(grades) > 0:
        average = sum(grades) / len(grades)
    else:
        average = 0
    student_averages[student] = average

print("1: Student Averages:")
print(student_averages)
print(" ")

# 2 Determine Letter Grades
student_letter_grades = {}
for student, average in student_averages.items():
    if 90 <= average <= 100:
        letter_grade = "A"
    elif 80 <= average < 90:
        letter_grade = "B"
    elif 70 <= average < 80:
        letter_grade = "C"
    elif 60 <= average < 70:
        letter_grade = "D"
    else:
        letter_grade = "F"
    student_letter_grades[student] = letter_grade

print("2: Student Letter Grades:")
print(student_letter_grades)
print(" ")

# 3 Top Performer
# Creates variables to keep track of the top student
top_student = None
highest_average = 0

for student, average in student_averages.items():
    if average > highest_average:
        highest_average = average
        top_student = student

print("3: Top Performer")
print(f"The top performer is {top_student} with an average of {highest_average:.2f}.")
print(" ")

# 4 Calculate and Display Class Statistics
# Calculates the overall class average
overall_average_sum = sum(student_averages.values())
class_average = overall_average_sum / len(student_averages)

# Counts the number of students passing
passing_students_count = 0
for letter_grade in student_letter_grades.values():
    if letter_grade in ["A", "B", "C"]:
        passing_students_count += 1

print("4: Calculate and Display Class Statistics")
print(f"Overall Class Average: {class_average:.2f}")
print(f"Number of students who passed (C or better): {passing_students_count}")
import this
