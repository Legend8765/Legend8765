import turtle

t=turtle.Turtle()

t.speed(2500)
turtle.bgcolor("blue")

for i in range(30000):
    t.color("cyan")
    t.circle(i)
    t.left(5)

turtle.done()          