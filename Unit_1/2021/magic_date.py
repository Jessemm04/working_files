#Q.19
#19. The date 10 June 1960 is special because the day times the month equals the year.
#Create a program that asks the user to enter a date in the format dd/mm/yy and output whether
#it is a magic date or not.
date = (input("Enter a date in the format of dd/mm/yy: "))

day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:len(date)])


if year == month * day:
    print(date, "is a magic date!")
else:
    print(date, "is not a magic date")