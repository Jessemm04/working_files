# x = 10
# while x > 0:
#     print(x)
#     x = x - 1
# print("Blast Off!")

# num = int(input("Enter a number -1 to exit: "))
# while num > 0:
#     if num % 2 == 0:
#         print('Even')
#     else:
#         print('Odd')
#     num = int(input("Enter a number -1 to exit: "))
# print("Bye")

# msg = "Hello world"
# c = 0
# while c < len(msg):
#     print(msg[c].upper())
#     c += 1

# w = 0
# while w % 10 != 2:
#     w = (w + 4) % 2
#     print("w=" + str(w))

#12.	The current population of Uganda is 26 million and its annual rate of growth is 3%. If it continues to grow
# at the same rate, how many years will it take to reach 50 million?

# population = 26
# years = 0
# while population < 50:
#     population = population * 0.03
#     years = years + 1
# print(years, population)

#print('It will take', years, 'years to reach a population of 50 million')

#13.	The greatest common divisor of two positive integers, A and B, is the largest number that can be evenly
# divided into both of them. Euclid’s algorithm can be used to find the greatest common divisor (GCD) of two positive
# integers. You can use this algorithm in the following manner:
#•	Compute the remainder of dividing the larger number by the smaller number.
#•	Replace the larger number with the smaller number and the smaller number with the remainder.
#•	Repeat this process until the smaller number is zero.
#•	The larger number at this point is the GCD of A and B.

A = int(input("Enter a positive integer: ").strip())
B = int(input("Enter a second positive integer: ").strip())
r = 0

while A > B:
    if B != 0:
        r = A % B
        A = B
        B = r
    print(A)
while B > A:
    if A != 0:
        r = B % A
        B = A
        A = r
    print(B)



