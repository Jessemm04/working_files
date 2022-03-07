#14.	Write a program which displays the factors of a number (a factor is a number that divides evenly into a
#number, leave out 1 because it is a factor of all numbers.

numb = int(input('Enter a number: '))
while numb != 'Quit':
    for n in range(2, numb+1):
        if numb % n == 0:
            print(n)
    numb = int(input('Enter a number: '))