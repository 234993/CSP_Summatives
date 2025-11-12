import turtle as trtl 
import random as rand
wn = trtl.Turtle()
wn.hideturtle()
wn = trtl.Screen()
square  = trtl.Turtle()
plus = trtl.Turtle()
times = trtl.Turtle()
minus = trtl.Turtle()
divide = trtl.Turtle()
plus.penup()

#Ask player for name 
player = trtl.textinput("Name:", "Hello what is your name?")
player = trtl.textinput("Message",  player +", Are you ready to escape to the zoo?")
player = player.lower()

if player == "n":
    wn.bye()
else:
    wn.bgpic("background.gif")
#display message with captured name 



# change background 
wn.addshape("plus.gif")
plus.penup()
plus.shape("plus.gif")

wn.addshape("times.gif")
times.penup()
times.shape("times.gif")

wn.addshape("minus.gif")
minus.penup()
minus.shape("minus.gif")

wn.addshape("divide.gif")
divide.penup()
divide.shape("divide.gif")

#set condtions for layout 
square.penup()
def place():
    square_list_color = ("blue", "yellow", "green", "pink", "purple", "red", "orange")
    square.shapesize(9)
    square.shape("square")
    square.color(rand.choice(square_list_color))
    square.penup()
    square.stamp()


divide.hideturtle()
plus.hideturtle()
minus.hideturtle()
times.hideturtle()
def symbol_set_up():
  plus.goto(100, -225)
  plus.stamp()  
  minus.goto(-100, -225)
  minus.stamp()
  times.goto(0, -25)
  times.stamp()
  divide.goto(-100, 175)
  divide.stamp()
  minus.goto(100, 175)
  minus.stamp()
  plus.goto(0, -425)
  plus.stamp()
  plus.goto(0, 375)
  plus.stamp()

square.goto(0, -425)
place()

square.goto(100, -225)
place()


square.goto(-100, -225)
place()


square.goto(0, -25)
place()

square.goto(-100, 175)
place()

square.goto(100, 175)
place()

square.goto(0, 375)
place()

symbol_set_up()
divide.showturtle()
plus.showturtle()
minus.showturtle()
times.showturtle()

#number list 
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#Leaderboard 




#Timer/timer limt for each problem  



#Set condtions for math problems 

#Restart/try again 

wn.listen()
wn.mainloop()