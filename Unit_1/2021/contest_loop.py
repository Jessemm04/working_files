#6.	Write a loop that will continuously input and print the names of contest participants, until
#QUIT is entered in place of the name.
name = str(input('Enter participants name: ').strip())
while name != 'QUIT':
    print(name)
    name = str(input('Enter participants name: ').strip())
print('Bye')