#Task 1 :  Read a File and Handle Errors

# Define the filename
filename = "sample.txt"

# open the file and read
try:
    with open(filename, 'r') as file:
        print("Reading file content:")
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
# when the file is not found   
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")







