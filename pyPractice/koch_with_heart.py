import turtle

def koch(size,n):
    turtle.speed(0)
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def heart():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(2,-100)
    turtle.pendown()
    turtle.color('red', 'pink')
    turtle.pensize(2)
    
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(111.65)
    
    curvemove()
    
    turtle.left(120)
    
    curvemove()
    
    turtle.forward(111.65)
    turtle.end_fill()
    turtle.hideturtle()
    
    turtle.done()

def curvemove():
    turtle.speed(0)
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
        

def main():
    turtle.setup(600,600)   #canvas size
    
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()    #start at (-200,100)
    turtle.pensize(2)


    level=3

    koch(400,level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    
main()
heart()