import turtle
s = turtle.Turtle()
cl=['white','red',]
for i in range(50):
    s.pensize(i)
    s.color(cl[i%2])
    s.setheading(50+i)
    s.forward(100+i*2)
    s.setheading(100+i)
    s.forward(100+i*2)
    s.setheading(-140+i)
    s.forward(100+i*2)
    s.setheading(-78+i)
    s.forward(120+i*2)
    s.speed(10)


turtle.done()
