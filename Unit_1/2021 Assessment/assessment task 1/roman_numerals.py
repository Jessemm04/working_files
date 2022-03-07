values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
numerals = " "
num = int(input('Enter a number between 1 and 3999: ').strip())

if num >= 1 and num <= 3999:
    for i in range(0,13):
        while num >= values[i]:
            num = num - values[i]
            numerals += (roman[i])
    print(numerals)
else:
    print('Error')