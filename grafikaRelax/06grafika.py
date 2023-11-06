import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
s.bgcolor('AntiqueWhite')
colors=['Brown', 'Crimson', 'Darksalmon', 'Blue', 'Lime', 'red']
for j in range (6):
    t.fillcolor(colors[j])
    t.pencolor(colors[j])
    t.begin_fill()
  
    for i in range (6):
        t.fd(100)
        t.rt(60)
    t.end_fill()
    t.fd(100)
    t.lt(60)
s.exitonclick()