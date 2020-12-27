import turtle as t

t.penup()
t.shape('turtle')
t.bgcolor('dodger blue')
t.speed('fast')

def rect(horizontal,vertical,color):
    t.pendown()
    t.color(color)
    t.begin_fill()
    for counter in range(0,2):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

def triangle(length,color):
    t.pendown()
    t.color(color)
    t.begin_fill()
    for c in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()
    t.penup()

t.goto(0,0)
rect(100,150,'yellow')

t.goto(0,100)
rect(100,50,'red')

t.goto(40,50)
rect(20,50,'grey')

t.goto(20,-150)
rect(10,150,'green')

t.goto(70,-150)
rect(10,150,'green')

t.goto(-20,-300)
rect(50,20,'blue')

t.goto(70,-300)
rect(50,20,'blue')

t.goto(-60,-20)
rect(60,20,'orange')

t.goto(100,-20)
rect(60,20,'orange')

#left eye
t.goto(20,90)
rect(5,5,'white')

#right eye
t.goto(75,90)
rect(5,5,'white')

t.goto(0,100)
triangle(100,'purple')

t.goto(-60,50)
rect(20,70,'orange')

t.goto(140,50)
rect(20,70,'orange')

t.goto(150,40)
t.begin_fill()
t.circle(20)
t.end_fill()

t.goto(-50,40)
t.begin_fill()
t.circle(20)
t.end_fill()

t.goto(50,55)
t.begin_fill()
t.circle(10)
t.end_fill()

t.hideturtle()
