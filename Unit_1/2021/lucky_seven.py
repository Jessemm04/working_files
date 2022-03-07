# Q.14
import random
pot = int(input('How much pot: '))
times = 0
max = pot
while pot > 0:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    if total == 7:
        pot += 4
        times += 1
    else:
        pot -= 1
        times += 1
    if pot > max:
        max = pot

print(times)
print(max)