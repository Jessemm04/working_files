#For every number between 1 and 100 inclusive, either print the number or if its a multiple of 3 print
# "fizz"
#if its a multiple of 5 print the word "buzz" if its a multiple of 3 and 5 print "fizzbuzz"
for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0 and x % 5 != 0:
        print("fizz")
    elif x % 5 == 0 and x % 3 != 0:
        print("buzz")
    else:
        print(x)