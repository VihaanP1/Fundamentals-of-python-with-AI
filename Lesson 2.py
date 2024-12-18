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

t.mainloop()