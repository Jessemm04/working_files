from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()

def talloval(r):               # Verticle Oval
    turtle.left(45)
    for loop in range(2):      # Draws 2 halves of ellipse
        turtle.circle(r,90)    # Long curved part
        turtle.circle(r/2,90)  # Short curved part

# Set initial position
turtle.penup()
turtle.left(165)
turtle.fd(250)
turtle.pendown()
turtle.pensize(15)
turtle.right(15)

# "I"
turtle.fillcolor("red")
turtle.begin_fill()
turtle.left(120)
turtle.fd(100)

# "L"
#turtle.penup()
turtle.left(150)
turtle.fd(115)
turtle.pendown()
turtle.pensize(4)

turtle.fillcolor("red")
turtle.begin_fill()
turtle.left(210)
turtle.fd(100)
turtle.left(90)
turtle.fd(50)

# "O"
#turtle.penup()
turtle.left(0)
turtle.fd(70)
turtle.left(90)
turtle.fd(10)
turtle.pendown()
turtle.pensize(4)

turtle.right(45)
for loop in range(2):
    turtle.circle(60,90)
    turtle.circle(60/2,90)

# "V"
#turtle.penup()
turtle.left(20)
turtle.fd(100)
turtle.right(130)
turtle.pendown()
turtle.pensize(4)

turtle.fd(100)
turtle.left(130)
turtle.fd(100)

# "E"
#turtle.penup()
turtle.right(65)
turtle.fd(80)
turtle.left(180)
turtle.pendown()
turtle.pensize(4)

turtle.fd(50)
turtle.left(90)
turtle.fd(45)
turtle.left(90)
turtle.fd(50)
turtle.right(180)
turtle.fd(50)
turtle.left(90)
turtle.fd(45)
turtle.left(90)
turtle.fd(50)

# "Y"
#turtle.penup()
turtle.right(90)
turtle.fd(65)
turtle.right(90)
turtle.fd(300)
turtle.pendown()
turtle.pensize(4)

turtle.left(130)
turtle.fd(65)
turtle.right(265)
turtle.fd(65)
turtle.right(180)
turtle.fd(65)
turtle.left(45)
turtle.fd(70)

# move pen to love heart position
#turtle.penup()
turtle.left(30)
turtle.fd(55)
turtle.left(90)
turtle.fd(100)
turtle.pendown()

# "<3"
def curve():
    for i in range(200):
        # Defining step by step curve motion
        turtle.right(1)
        turtle.forward(0.5)

# Set the fill color to red
turtle.fillcolor('red')
# Start filling the color
turtle.begin_fill()
# Draw the left line
turtle.left(140)
turtle.forward(56.5)

# Draw the left curve
curve()
turtle.left(120)

# Draw the right curve
curve()

# Draw the right line
turtle.forward(55.5)

# Ending the filling of the color
turtle.end_fill()

# "U"
#turtle.penup()
turtle.left(130)
turtle.fd(80)
turtle.left(90)
turtle.fd(75)
turtle.pendown()

turtle.right(200)
turtle.fd(65)
turtle.circle(40,180)
turtle.fd(65)

#turtle.penup()
turtle.fd(300)
turtle.right(90)
turtle.fd(200)
turtle.left(90)
turtle.pendown()

#Rose

# Set initial position
#turtle.penup()
turtle.left(90)
turtle.fd(200)
turtle.pendown()
turtle.right(90)

# flower base
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(10, 180)
turtle.circle(25, 110)
turtle.left(50)
turtle.circle(60, 45)
turtle.circle(20, 170)
turtle.right(24)
turtle.fd(30)
turtle.left(10)
turtle.circle(30, 110)
turtle.fd(20)
turtle.left(40)
turtle.circle(90, 70)
turtle.circle(30, 150)
turtle.right(30)
turtle.fd(15)
turtle.circle(80, 90)
turtle.left(15)
turtle.fd(45)
turtle.right(165)
turtle.fd(20)
turtle.left(155)
turtle.circle(150, 80)
turtle.left(50)
turtle.circle(150, 90)
turtle.end_fill()

# Petal 1
turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)

# Petal 2
turtle.left(180)
turtle.circle(90, 40)
turtle.circle(-80, 98)
turtle.setheading(-83)

# Leaves 1
turtle.fd(30)
turtle.left(90)
turtle.fd(25)
turtle.left(45)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(-80, 90)
turtle.right(90)
turtle.circle(-80, 90)
turtle.end_fill()
turtle.right(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(85)
turtle.left(90)
turtle.fd(80)

# Leaves 2
turtle.right(90)
turtle.right(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(80, 90)
turtle.left(90)
turtle.circle(80, 90)
turtle.end_fill()
turtle.left(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(60)
turtle.right(90)
turtle.circle(200, 60)

screen.exitonclick()