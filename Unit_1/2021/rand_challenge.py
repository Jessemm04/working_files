#produce
#1
#22
#333
#4444
#55555

# for i in range(1,6,1): #loop for each line
#     line = " " #line string
#     for x in range(1, i+1):
#         line += str(i)
#     print(line)

#produce
#
##
###
####
#####

# for i in range(1,6,1): #loop for each line
#     line = "#" #line string
#     for x in range(i, i+i):
#         line = line + x
#     print(line)

#produce
#####
####
###
##
#

#produce
#
# _#
# __#
# ___#
# ____#
# digit = '#'
# for i in range(5): #loop for each line
#      line = " " #line string
#      for x in range(0, i):
#          line = line + '_'
#      line = line + '#'
#      print(line)

# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# 4 8 12 16 20 24 28 32 36 40
# 5 10 15 20 25 30 35 40 45 50

# for i in range(1, 6):
#     line = " "
#     for x in range(1, 11):
#         line += str(i * x) + " "
#     print(line)


# ....1
# ...22
# ..333
# .4444
# 55555

# for i in range(1, 6):
#     line = " "
#     for x in range(0, 5-i):
#         line += "."
#     for k in range(0,i):
#         line += str(i)
#     print(line)

#15.	Write a program which finds and displays the 'perfect numbers' up to a user-supplied value.
# (A perfect number is one whose factors add up to the number itself, eg 6 = 1+2+3.)


num = int(input('Enter a number: ').strip())
perfect_num = 0
for n in range(1, num):
    if num % n == 0:
        perfect_num = perfect_num + n
if perfect_num == num:
    print(num, 'is a perfect number.')
else:
    print(num,"is not a perfect number")


num = int(input('Enter the max number: ').strip())
for n in range(1, num+1):
    total = 0
    factors = " "
    for x in range(1, n):
        if n % x == 0:
            total += x
            factors += str(x) +" "
    if total == n:
        print(i, "is a perfect number ->1 factors:", factors)