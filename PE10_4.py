"""
4. Print Arbitrary Values 
a) Define a function printNames() with a parameter names. 
The names parameter builds a tuple of any number of argument values. 
This function prints all contents of the names tuple. 
b) Call the function printNames() with any number of name arguments (see output below). 
Example Output  
Ann Bianca Coco Dora Emily
"""

def printNames(*names):
    for n in names:
        print(n, end=" ")
    print()

def main():
    printNames("Ann", "Bianca", "Coco", "Dora", "Emily")

main()
