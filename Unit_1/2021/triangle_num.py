#12. Write a program which outputs triangle numbers - 1, 3, 6, 10,15, etc. We initialise a
# variable to 0 and then add the loop counter to it during each pass through the loop. The value of the
# number changes thus: 0, 0+1, 1+2, 3+3, 6+4, 10+5, etc

number = int(input('Enter number of loops: '))
loop = 0
for n in range(number):
    loop += n
    print(loop)