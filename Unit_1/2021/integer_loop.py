#9.	The factorial of an integer N is the product of all of the integers between 1 and N, inclusive.
# For example if N = 5 then the factorial would be 1*2*3*4*5.
# Write a while loop that computes the factorial of a given integer N.

N = int(input('Enter an integer: '))
factorial = 1
i = 1
while i <= N:
    factorial = factorial * i
    i += 1
print(factorial)


