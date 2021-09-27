import turtle

def circle(x,y,r):
    turtle.penup()
    turtle.goto(x,y-r)
    turtle.pendown()
    turtle.circle(r)
def makePicture(x,y,r):

    if r < 10:
        circle(x, y, r)
    else:
        circle(x, y, r)
        makePicture(x + r, y, r / 2)
        makePicture(x - r, y, r / 2)
makePicture(0,0,200)
turtle.done()

