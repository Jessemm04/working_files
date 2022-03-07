#simulat the drawing of 6 random balls between 1 and 45.
# obviously you cannot have the same number twice. output the numbers of lowest to highest.
import random
balls = []

for i in range(6):
    b = random.randint(1, 45)
    while b in balls:
        b = random.randint(1,45)
    balls.append(b)
balls.sort()
print(balls)

#or

balls = []
while len(balls) < 6:
    b = random.randint(1, 45)
    if b not in balls:
        balls.append(b)

balls.sort()
print(balls)

#Homework - finish reading 10.1