import turtle
s = turtle.Turtle()
cl=['green','red']
for i in range(100):
    s.color(cl[i%2]) 
    s.circle(100)
    s.pensize(5)
    s.setheading(i*20)
    s.speed(100) #makes the turtle move faster
turtle.done()
