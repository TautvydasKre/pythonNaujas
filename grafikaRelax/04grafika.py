import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
s.bgcolor('yellow')
t.fillcolor('blue')


t.penup()
t.goto(0, -300)
t.pendown()
colors=['AntiqueWhite','Brown', 'Coral','Crimson', 'Darksalmon', 'Goldenrod', 'Ivory', 'Lime']
t.pencolor(colors[0])
for j in range(20, 2, -1):
    t.fillcolor(colors[(j+1)%7])
    t.pencolor(colors[j%7])
    t.begin_fill()
    for i in range(j):
        t.fd(100)
        t.lt(360/j)
    t.end_fill()

# for i in range (3):
#     t.fd(100)
#     t.lt(120)
# for i in range (4):
#     t.fd(100)
#     t.lt(90)
# for i in range (5):
#     t.fd(100)
#     t.lt(72)
# for i in range (6):
#     t.fd(100)
#     t.lt(60)
# for i in range (7):
#     t.fd(100)
#     t.lt(51)
# for i in range (8):
#     t.fd(100)
#     t.lt(45)
# for i in range (9):
#     t.fd(100)
#     t.lt(40)
# for i in range (10):
#     t.fd(100)
#     t.lt(36)
# for i in range (11):
#     t.fd(100)
#     t.lt(32)
# for i in range (12):
#     t.fd(100)
#     t.lt(30)







s.exitonclick()