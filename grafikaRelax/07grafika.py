import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
s.bgcolor('AntiqueWhite')
colors=['Brown', 'Crimson', 'Darksalmon', 'Blue', 'Lime']
def kvadratas():
    for i in range(4):
        t.color('red')
        t.fd(100)
        t.lt(360/4)
    

for j in range (5):
    t.penup()
    x= x+200
    t.goto(x, -250)
    t.pendown()
    



s.exitonclick()