import turtle as t
t.speed (0)
t.bgcolor ("grey")
t.width (3)

t.color ("white", "#cccbca")
t.begin_fill()
for x in range (36):
    t.forward(15)
    t.right(10)
t.end_fill()

t.color ("white", "#cccbca")
t.begin_fill()
for x in range (36):
    t.forward(12)
    t.left(10)
t.end_fill()

t.color ("white", "#cccbca")
t.penup()
t.goto(10, 137)
t.pendown()
t.begin_fill()
for x in range (36):
    t.forward(7)
    t.left(10)
t.end_fill()

t.penup()
t.goto(2, 192)
t.pendown()
t.color ("black")
t.begin_fill()
for x in range (36):
    t.forward(0.5)
    t.right(10)
t.end_fill()

t.penup()
t.goto(25, 192)
t.pendown()
t.color ("black")
t.begin_fill()
for x in range (36):
    t.forward(0.5)
    t.right(10)
t.end_fill()

t.penup()
t.goto(13.5, 175)
t.pendown()
t.color ("darkorange")
t.begin_fill()
for x in range (36):
    t.forward(0.75)
    t.right(10)
t.end_fill()

t.setheading(270)
t.penup()
t.goto(-1.5, 160)
t.color("black")
t.pendown()
t.circle(15,180)

t.penup()
t.goto(-63, 73)
t.pendown()
t.setheading(230)
t.forward(105)

t.penup()
t.goto(75, 73)
t.pendown()
t.setheading(310)
t.forward(105)

t.mainloop()
