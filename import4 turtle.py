import turtle

t = turtle.Turtle()

t.speed(10)
turtle.bgcolor("blue")

for i in range(1000):
    t.color("red")
    t.circle(1)
    t.left(10)

    turtle.done()