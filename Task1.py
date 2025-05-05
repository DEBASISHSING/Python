# Creates a dictionary where student names are keys and their marks are values.
student_marks = {"Debasish": 80, "Ashish": 70, "Subhasish": 60, "Sish": 50}

# Asks the user to input a student's name.
name = input("Enter the student's name: ")

# Retrieves and displays the corresponding marks,  If the student’s name is not found, display an appropriate message.

marks = student_marks.get(name)
if marks:
    print(f"{name}'s marks: {marks}")
else:
    print("Student not found.")









