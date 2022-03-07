#10.	The game “3X+1” goes like this.  If N is odd, multiply it by 3 and add 1.  If N is even, divide it by 2.
# Repeat until N equals 1, if ever.  Every value of N that anyone has ever checked eventually leads to 1,
# but it is an open mathematical problem (known as the Collatz conjecture) whether EVERY value of N eventually
# leads to 1.  It is also called 3n+1, and you can read about it on Wikipedia.  Before you start working on these
# programs, take a sheet of paper and write out what happens when you start with N=5, N=6, N=7, N=9, to get a feel
# for it.  For example, starting with N=6, the next number is 3, then 10, then 5, then 16, 8, 4, 2, 1 and we are done.

# N = int(input("Enter the number: "))
#
# while N != 1:
#     print(N)
#     if N % 2 == 0:
#         N = N // 2
#     else:
#         N = N * 3 + 1
# print(N)


