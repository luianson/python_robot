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

t.hideturtle()
