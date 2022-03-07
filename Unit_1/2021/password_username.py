#15.Write a program that prompts the user to enter their user name and password.
# It should check these against values of your choosing. If these values are correct, it should display
# “welcome back, you are logged in”. If they are wrong, it should display “either username or password is incorrect”.
# If they have tried 3 times and got it wrong, your program should display “your account is now locked out for
# 60 minutes”.
user_input = str(input('Enter your user name: ').strip())
password_input = str(input('Enter your password: ').strip())
username = "jSemmler"
password = "12345"
times = 3

if user_input == username and password_input == password:
    print("Welcome back, you are logged in.")


while True:
    if user_input != username or password_input != password:
        print("Either username or password is incorrect. Try again")
        user_input = str(input('Enter your user name: ').strip())
        password_input = str(input('Enter your password: ').strip())
    print('Your account is now locked out for 60 minutes.')
    if user_input == username and password_input == password:
        print("Welcome back, you are logged in.")




# tests_passed = 0
# valid_password = True
# lc = False
# uc = False
# num = False
# special = False
# if len(password) < 6 or len(password) > 20:
#     valid_password = False
#     print("Password must be at least 6 characters")
# for character in password:
#     if character.islower():
#         lc = True
#     if character.isupper():
#         uc = True
#     if character.isdigit():
#         num = True
#     if not character.isalnum():
#         special = True
# if lc == True:
#     tests_passed = tests_passed + 1
# if uc == True:
#     tests_passed += 1
# if num is True:
#     tests_passed += 1
# if special is True:
#     tests_passed += 1
# if valid_password is True and tests_passed >= 3:
#     print("Your password has been accepted")
# else:
#     print("You need to include", 3 - tests_passed, "of the following")
#     if lc == False:
#         print("A lowercase letter")
#     if uc == False:
#         print("An uppercase letter")
#     if num is False:
#         print("A number")
#     if special is False:
#         print("A special character")