"""
Data Management Functions
2. Name format
a) Define a function nameFormat() with parameters first, middle, and last.
1) This function prints the first name, the middle initial and the last name using proper title format.
b) Define a main() function to do the following:
1) Call the function nameFormat with these positional arguments: john stu smith
2) Call the function nameFormat with these keyword arguments:
last = ‘kennedy’, first = ‘john’, middle = ‘fitzgerald’
c) Call main() function to initiate the tasks to be performed

"""
def nameFormat(first, middle, last):
    middle_initial = middle[0].upper() + "."
    print(first.title(), middle_initial, last.title())

def main():
    nameFormat("john", "stu", "smith")

    nameFormat(first="john", middle="fitzgerald", last="kennedy")

main()










