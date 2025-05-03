# Task 2: Write and Append Data to a File

# Take user input and write it to output.txt
write_text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(write_text  +"\n" )
print("Data successfully written to output.txt.")

# Take additional input and append it to the file
append_text = input("\nEnter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_text + "\n")
print("Data successfully appended.")

# Read and display
print("\nFinal content of output.txt:")
with open("output.txt", 'r') as file:
    Write_appand = file.read()
    print(Write_appand )
