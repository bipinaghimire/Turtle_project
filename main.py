import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
screen = turtle.Screen()
pen= turtle.Turtle()
pen.shape('turtle')
turtle.bgcolor('black')
pen.fillcolor('yellow')
pen.speed(10)
for i in range(300):
    pen.pencolor(colors[i%6])
    pen.width(4)
    pen.forward(i)
    pen.left(90)
turtle.done()