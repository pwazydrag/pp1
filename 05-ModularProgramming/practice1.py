#8
X=10
Y=10
N=25

def drawSquare(x,y,n):
    import turtle
    #turtle.penup()
    #turtle.setpos(x,y)
  #  turtle.setx(x)
   # turtle.sety(y)
    #turtle.pendown()
    for o in range (0,4):
        turtle.forward(n)
        turtle.right(90)
    #print(turtle.position())
    turtle.forward(n)
    #turtle.done()
#9
def square16(x,y,n):
    import turtle
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    for b in range (0,4):
        for a in range (0,4):
            drawSquare(X,Y,N)
        turtle.right(180)
        turtle.forward(4*n)
        turtle.left(90)
        turtle.forward(n)
        turtle.left(90)
  #  turtle.right(90)
   # turtle.forward(n)
    turtle.done()    
square16(X,Y,N)

        
        
