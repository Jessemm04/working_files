
num = (input('Enter a number between 1 and 999: ').strip())


#for x in str(num):
n = num.split('\n')

sum = int()
if len(str(num)) == [3]:
    n1 = int(n[0])
    n2 = int(n[1])
    n3 = int(n[2])
    sum = (int(n1 * n1) + (n2 * n2) + (n3 * n3))

elif len(str(num)) == [2]:
    n1 = int(n[0])
    n2 = int(n[1])
    sum = (int(n1 * n1) + (n2 * n2))

elif len(str(num)) == [1]:
    n1 = int(n[0])
    sum = int(n1 * n1)

n = int(num)

for sum in range(n):

    if sum != 1:
        print("The sum of", num, "is", sum, 'This is an Unhappy number')
    else:
        print("The sum of", num, "is", sum, 'This is a Happy number')