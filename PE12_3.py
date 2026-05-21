"""
3. File Appending
Write a program that adds/appends lines to the end of an existing file.
"""

def append_presidents():
#open the file in append mode so we can add more names at the end
    with open("Presidents.txt", "a") as file_object:
        file_object.write("James Madison\n")
        file_object.write("James Monroe\n")
        file_object.write("John Quincy Adams\n")
#open the file again so we can read everything inside it
    with open("Presidents.txt", "r") as file_object:
        print("Presidents.txt")
        for line in file_object:
            print(line.rstrip())

#run the function so the names get added and printed
append_presidents()

