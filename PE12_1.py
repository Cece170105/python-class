#creating a file
#using loop
filename = 'presidents.txt'
with open("C:/Users/marin/Downloads/PE12/presidents.txt") as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

#making a list
filename = 'presidents.txt'
with open ("C:/Users/marin/Downloads/PE12/presidents.txt") as file_object:
    lines = file_object.readlines()
print("".join(lines))
