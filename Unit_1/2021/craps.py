import random

#number of rolls + 7
#craps = 7
#number of rolls - 7

rolls = int(input('How many dice rolls?: '))
craps = 0
over = 0
under = 0
for r in range(rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_add = dice1 + dice2
    if dice_add == 7:
        craps =+1
    elif dice_add > 7
        over =+1
    else:
        under =+ 1
print('Under:', under)
print('Over:', over)
print('Craps:', craps)