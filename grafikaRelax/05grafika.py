import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
s.bgcolor('AntiqueWhite')
colors=['Brown', 'Crimson', 'Darksalmon', 'Blue', 'Lime']
x = -700
for j in range (5):
    t.penup()
    x= x+200
    t.goto(x, -250)
    t.pendown()
    for i in range (4):
        t.pencolor(colors[j%5])
        t.fd(100)
        t.rt(90)



s.exitonclick()