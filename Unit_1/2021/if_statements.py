# age = int(input("Enter your age: "))
# runagain = "yes"
# if age >= 18:
#     print("You can buy alcohol")
# else:
#     print("You are not old enough. You cannot buy alcohol")

# vowels = 'aeiou'
# word = input('Please eneter a word: ')
# Last_letter = word[-1].lower()
#
# if Last_letter in vowels:
#     print("your word ends in a vowel")
# else:
#     print("Your word ends in a consonant")

# mark = (input("Enter your mark: ").strip()
# if mark.isdigit():
#     mark = int(mark)
#     if mark > 100:
#         print("That is not a valid grade")
#     else:
#         if mark >= 80:
#             grade = 'A'
#         elif mark >= 70:
#             grade = 'B'
#         elif mark >= 50:
#             grade = 'C'
#         elif mark >= 30:
#             grade = 'D'
#         else:
#             grade = 'E'
#         print('Your grade is:', grade)
# else:
# print("Type a number not letters")

# number = (input('Enter a series of random numbers: ')).strip
# if number.isdigit():
#     total = 0
#     for n in number:
#         total = total + int(n)
#     print(total)
# else:
#     print('Enter numbers only')

#10, 000 or more, commision: 10%, less than 10, 000, comission is 5%

# sales = int(input("Enter sales: ")).strip()
# if sales.isdigit():
#     commission = 0
#     if sales >= 10000:
#         commission = sales * 0.10
#     else:
#         commission = sales * 0.05
#     print(commission)
# else:
#     print("Enter number for sales")

# hw task:
 #   ask user to enter a word. if word has even number of letters, print first half of word, and the second half of the word.
 # e.g 'swimming'. get length and d modulest division by 2. if odd number, print middle letter.

# word = str(input("Enter a word: "))
#
# if [len(word) % 2 == 0]:
#     print(word[0:len(word) // 2])
#     print(word[len(word) // 2:])
# else:
#     print(word[len(word)//2])

#pig latin: move the first letter to the end, then add 'AY' to the end of it
# use lists

#word = str(input('Enter a word: '))

#password must be 6 characers and at most 20. must contain at least 3:
# lowercase, upper case, one number, one special character

# password = (input('Enter a password: '))
# correct_password = True
#
# lower = False
# upper = False
# special = False
# number = False
# error = "Password must "
#
# if len(password) < 5 or len(password) > 19:
#     correct_password = False
#     tests = 0
#     print(error + 'be greater than 6 characters and shorter than 20 characters ')
#
# for character in password:
#     if character.islower():
#         lower = True
#     if character.isupper():
#         upper = True
#     if character.isdigit():
#         number = True
#     if character.isalnum():
#         special = True
#
# if lower == False:
#     print(error + 'have a lower case')
# if upper == False:
#     print(error + 'have an upper case')
# if number == False:
#     print(error + 'have a number')
# if special == False:
#     print(error + 'have a special character')
#
# if lower == True:
#     tests +=1
# if upper == True:
#     tests += 1
# if number == True:
#     tests += 1
# if special == True:
#     tests += 1
#
# if correct_password == True and tests => 3:
#     print('Password accepted')

#get the month
month = int(input('Enter the month.'))
#validate the month
while month < 1 or month > 12:
   print('ERROR: The month cannot be less than 1 or greater than 12.')
   month = int(input('Enter the correct month.'))

#get the day
day = int(input('Enter the day.'))
#validate the day
while day < 1 or day > 31:
   print('ERROR: The day cannot be less than 1 or greater than 31.')
   day = int(input('Enter the correct day.'))

#get the year
year = int(input('Enter the year.'))
#validate the year
while year < 0 or year > 99:
   print('ERROR: The year cannot be less than 00 or greater than 99.')
   year = int(input('Enter the correct year.'))

#determine if the date is magic or not
if year == month * day:
   print('Magic Date')
else:
   print('Not a Magic Date')

