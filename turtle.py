import turtle

wn = turtle.Screen()
wn.bgcolor("green")


def draw_sqr(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)


alex = turtle.Turtle()
draw_sqr(alex, 50)

alex.penup()
alex.goto(75, 75)
alex.pendown()
draw_sqr(alex, 100)

alex.penup()
alex.goto(-150, -150)
alex.pendown()
draw_sqr(alex, 100)

alex.penup()
alex.goto(75, -75)
alex.pendown()
draw_sqr(alex, 100)

alex.penup()
alex.goto(-150,150)
alex.pendown()
draw_sqr(alex, 100)

wn.exitonclick()
