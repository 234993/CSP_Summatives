import turtle as trtl
# create the background
screen = trtl.Screen() # makes the screen bigger
screen.setup(width=1.0, height=1.0) #makes the screen bigger
trtl.bgcolor("midnight blue") 

#create grass-----------------------------------------------------------------------------------------------------------------------------
g = trtl.Turtle()
g.hideturtle()
g.pensize(300)
g.pencolor("DarkOliveGreen4")
g.penup()
g.goto(-1000,-300)
g.pendown()
g.forward(1700)

#create stars and moon ----------------------------------------------------------------------------------------------------------------
# create moon 
trtl.speed(100)
trtl.hideturtle() 
trtl.penup()
trtl.goto(300,100)
trtl.pendown()
trtl.pencolor("cornsilk2")
trtl.pensize(50)
trtl.begin_fill()
trtl.circle(100)
trtl.fillcolor("cornsilk2")
trtl.end_fill()

# create the tree-------------------------------------------------------------------------------------------------------------------------

#create tree trunk
trtl.color("orange4")
trtl.hideturtle()
trtl.penup()
trtl.goto(300,-300)
trtl.pendown()
trtl.begin_fill()
trtl.circle(300,140)
trtl.right(140)
trtl.forward(200)
trtl.right(90)
trtl.forward(550)
trtl.right(90)
trtl.forward(390)
trtl.fillcolor("orange4")
trtl.end_fill()
trtl.update() # I dont want to see the truck being drawn 

#create leaves 
leave_colors = ["DarkRed","DarkGoldenrod2","DarkOrange"]
trtl.hideturtle()
trtl.penup()
trtl.hideturtle()
trtl.goto(450,300)
trtl.pensize(0)
leave_x = trtl.xcor()
leave_y = trtl.ycor()



# repates the leaves 
for r in range(7):
    for l in leave_colors * 3:
        trtl.fillcolor(l)
        trtl.pendown()
        trtl.begin_fill()
        trtl.circle(50)
        trtl.end_fill()
        leave_x += 50
        trtl.penup()
        trtl.goto(leave_x, leave_y)
        trtl.pendown()
    leave_x = 400 
    leave_y += 30
    trtl.penup()
    trtl.goto(leave_x, leave_y)
    trtl.pendown()



#make the pumpkin -----------------------------------------------------------------------------------------------------------------------
# make body 
p = trtl.Turtle()
p.hideturtle()
p.pencolor("DarkOrange")
p.speed(0)
p.penup()
p.goto(-100, -300)
p.pendown()
p.fillcolor("DarkOrange")
p.begin_fill()
p.circle(200)
p.end_fill()   


# ask for eye ones shape 

eye_shape1 = screen.textinput("Eye Shape","What shape would you like one of the pumpkins eyes?(circle, triangle, or square)")

e = trtl.Turtle()
e.hideturtle() 
e.penup()
e.goto(-30,-100)
e.pendown()
e.pencolor("DarkGoldenrod1")
e.fillcolor("gold")
e.begin_fill()

if eye_shape1.lower() == "circle": #added .lower for error handling, can do upper and lower case 
    e.circle(50)
elif eye_shape1.lower() == "triangle":
    e.setheading(180)
    e.penup()
    e.goto(30,-100)
    e.pendown()
    for _ in range(3):
        e.forward(100)
        e.right(120)
elif eye_shape1.lower() == "square":
    e.setheading(180)
    e.penup()
    e.goto(30,-100)
    e.pendown()
    for _ in range(4):
        e.forward(100)
        e.right(90)
e.end_fill()


# ask for eye twos shape
e_2 = trtl.Turtle()
eye_shape2 = screen.textinput("Eye Shape","What shape would you like for the other pumpkins eye?(circle, triangle, or square)")

e_2.fillcolor("gold")
e_2.hideturtle() 
e_2.penup()
e_2.pencolor("DarkGoldenrod1")
e_2.goto(-200,-100)
e_2.pendown()
e_2.begin_fill()
if eye_shape2.lower() == "circle":
    e_2.circle(50)
elif eye_shape2.lower() == "triangle":
    e_2.setheading(180)
    e_2.penup()
    e_2.goto(-150,-100)
    e_2.pendown()
    for _ in range(3):
        e_2.forward(100)
        e_2.right(120)
elif eye_shape2.lower() == "square":
    e_2.setheading(180)
    e_2.penup()
    e_2.goto(-150,-100)
    e_2.pendown()
    for _ in range(4):
        e_2.forward(100)
        e_2.right(90)
else:
    e_2.circle(50)
e_2.end_fill()


# ask for nose shape----------------------------------------------------------------------------------------------------------------------
n = trtl.Turtle()
nose_shape = screen.textinput("Nose Shape","What shape would you like for the pumpkins nose?(circle, triangle, or square)")

n.fillcolor("gold")
n.hideturtle() 
n.pencolor("DarkGoldenrod1")
n.penup()
n.goto(-100,-135)
n.pendown()
n.begin_fill()
if nose_shape.lower() == "circle":
    n.circle(30)
elif nose_shape.lower() == "triangle":
    n.setheading(180)
    n.penup()
    n.goto(-100,-135)
    n.pendown()
    for nn in range(3):
        n.forward(30)
        n.right(120)
elif nose_shape.lower() == "square":
    n.setheading(180)
    n.penup()
    n.goto(-100,-135)
    n.pendown()
    for nn in range(4):
        n.forward(30)
        n.right(90)
else:
    n.circle(30)
n.end_fill()


# create mouth----------------------------------------------------------------------------------------------------
m = trtl.Turtle()
m.hideturtle()
m.setheading(270)
m.hideturtle() 
m.fillcolor("DarkGoldenrod1")
m.begin_fill()
m.pencolor("DarkGoldenrod1")
m.penup()
m.goto(-200,-160)
m.pendown()
m.circle(100,180)
m.right(270)
m.forward(200)
m.end_fill()


#create steam---------------------------------------------------------------------------------------
stem = trtl.Turtle()
stem.hideturtle()
stem.fillcolor("DarkGreen")
stem.begin_fill()
stem.pencolor("DarkGreen")
stem.penup()
stem.goto(-135,135)
stem.pendown()
for stemm in range(4):
        stem.forward(50)
        stem.right(90)
stem.end_fill()

#create stars ---------------------------------------------------------------------------------------------------------------------------
#create custom the turtle
star_t = trtl.Turtle()
trtl.addshape("star",((-10,10),(-2,0),(-10,-10),(0,-2),(10,-10),(2,0),(10,10),(0,2)))
star_t.penup()
star_t.hideturtle()
star_t.goto(-200,200)
star_t.showturtle()
star_t.shape("star")
star_t.turtlesize(4)
star_t.color("gold")


for l in range(10):
    star_t.forward(60)
    trtl.update()
    screen.ontimer(5.0)#slows down the star

screen.mainloop()
