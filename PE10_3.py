"""
3. Name format
a) Define a function nameFormat() with parameter first, last and middle where middle is an optional parameter.
If all three names are provided return: Last, First, M.
If only first and last are provided return: Last, First
b) Define a main() function to do the following:
1) Call the function with keyword arguments for the name: james bond
2) Call the function with keyword arguments for the name: henry indiana jones
3) Print the results of the function calls.
c) Call main() function to initiate the tasks to be performed.
"""
def nameFormat(first, last, middle=""):
    if middle: 
        middle_initial = middle[0].upper() + "."
        return f"{last.title()}, {first.title()}, {middle_initial}"
    else:
        return f"{last.title()}, {first.title()}"

def main():
    result1 = nameFormat(first="james", last="bond")

    result2 = nameFormat(first="henry", middle="indiana", last="jones")

    print(result1)
    print(result2)

main()