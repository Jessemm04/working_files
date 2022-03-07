# bmi(body mass index) is calculated as a persons weight(kg), divided by the square of the persons height(m)
#a bmi in the range 18.5-24.9 inclusive is considered healthy
#claculate a persons bmi and print a message saying if they are above, within, or below the healthy range

weight = float(input('Enter your weight in kg: ').strip())
height = float(input('Enter your height in metres: ').strip())
bmi = weight / (height * height)

if bmi < 18.5:
    print('Your BMI is', bmi, 'You are below the healthy range.')
if bmi > 24.9:
    print('Your BMI is', bmi, 'You are above the healthy range.')
elif bmi >= 18.5 and bmi <= 24.9:
    print('Your BMI is', bmi, 'You are within the healthy range')