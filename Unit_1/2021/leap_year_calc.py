#10. A year is a leap year if it is divisible by 4, and if it is a century,
# it must also be divisible by 400. (1800 and 1900 are not leap years while 1600 and 2000 are).
# Write a program that calculates whether a year is a leap year.
leapyear = False
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leapyear = True
        else:
            leapyear = False
    else:
        leapyear = False
else:
    leapyear = False

if leapyear == True:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")