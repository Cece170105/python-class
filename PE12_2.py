"""
2. File Writing
Write a program that defines two different functions to create files
"""

def create_file1():
#make the file Presidents2.txt and put two names in it
    with open("Presidents2.txt", "w") as file_object:
        file_object.write("George Washington\n")
        file_object.write("John Adams\n")
#open the file again so we can read it and print it
    with open("Presidents2.txt", "r") as file_object:
        print("Presidents2.txt")
        for line in file_object:
            print(line.rstrip())


def create_file2():
#make the file Presidents3.txt and put three names in it
    with open("Presidents3.txt", "w") as file_object:
        file_object.write("George Washington\n")
        file_object.write("John Adams\n")
        file_object.write("Thomas Jefferson\n")
#open the file again so we can read it and print it
    with open("Presidents3.txt", "r") as file_object:
        print("Presidents3.txt")
        for line in file_object:
            print(line.rstrip())

#run the functions so the files get made and printed
create_file1()
print()
create_file2()
