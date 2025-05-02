#Task 1

file1 = "my_file.txt"

with open(file1, 'r') as file:
    print("Reading file content: ")
    line_number = 1
    for line in file:
        print(f"Line {line_number}: {line.strip()}")
        line_number += 1



