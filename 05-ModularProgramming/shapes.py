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
#12a    
def drawCircle(x,y,r):
    import turtle
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.circle(r)
    turtle.done()
#drawCircle(100,100,100)
#12b
def drawTriangle60(x,y,a):
    import turtle
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.done()
#drawTriangle60(200,200,100)
#12c
def drawStar(n):
    import turtle
    turtle.color("black")
    turtle.begin_fill()
    for a in range (0,5):
        turtle.forward(n)
        turtle.right(144)
    turtle.end_fill()
#drawStar(100)
#12d
def drawFilledSquare(x,y,m):
    import turtle
    turtle.color("black")
    turtle.begin_fill()
    drawSquare(x,y,m)
    turtle.end_fill()
#drawFilledSquare(100,100,200)
#12e
def drawSquare12e(m):
    import turtle
    for o in range (0,4):
        turtle.forward(m)
        turtle.right(90)
def drawFilledSquare12e(m):
    import turtle
    turtle.color("black")
    turtle.begin_fill()
    drawSquare12e(m)
    turtle.end_fill()    
def drawSzachownica(m):
    import turtle
    count=0
    for b in range (0,8):
        if count%2==0:
            for a in range (0,4):
                drawSquare12e(m)
                turtle.forward(m)
                drawFilledSquare12e(m)
                turtle.forward(m)
            turtle.right(90)
            turtle.forward(m)
            turtle.right(90)
            turtle.forward(8*m)
            turtle.right(180)
            count+=1
        elif count%2==1:
            for c in range (0,4):
                drawFilledSquare12e(m)
                turtle.forward(m)
                drawSquare12e(m)
                turtle.forward(m)
            turtle.right(90)
            turtle.forward(m)
            turtle.right(90)
            turtle.forward(8*m)
            turtle.right(180)
            count+=1
#drawSzachownica(25)