import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.speed(8) #1 letas 3 greitesnis 5 normalus 10 greitas 0 greiciausias
s.bgcolor('yellow')
s.title('Pirmas kartas')

t.pen(pencolor='red', fillcolor='silver', pensize=9)


t.pensize(5)
t.pencolor('red')




t.begin_fill()
# t.color('green')
for i in range(5):
    t.lt(72)
    t.fd(100)
t.penup()
# t.fd(100)
t.pendown()
t.end_fill()

# t.goto(150,150)
# t.fillcolor('green')
# for i in range(5):
#     t.lt(72)
#     t.fd(100)


s.exitonclick()