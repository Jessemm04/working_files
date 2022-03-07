speed = int(input("Enter your speed: ").strip())

fine = 0
if speed <= 100:
    print("No fine is needed")
else:
    fine = (speed - 100) * 5 + 50
if speed >= 120:
    fine = fine + 200

print('Your fine is: $', fine)
