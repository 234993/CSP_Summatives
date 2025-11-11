import turtle as trtl 
import random as rand
wn = trtl.Turtle()
wn.hideturtle()
wn = trtl.Screen()
square  = trtl.Turtle()
plus = trtl.Turtle()
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



#set condtions for layout 
square.penup()
def place():
    square_list_color = ("blue", "yellow", "green", "pink", "purple", "red", "orange")
    square.shapesize(9)
    square.shape("square")
    square.color(rand.choice(square_list_color))
    square.penup()
    square.stamp()

def plussymbol():
    wn.addshape("plus.gif")
    plus.penup()
    plus.shape("plus.gif")
    plus.stamp()

square.goto(0, -425)
place()
plus.goto(0, -425)
plussymbol()

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
plus.goto(0, 375)
plussymbol()
#number list 
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#Leaderboard 




#Timer/timer limt for each problem  



#Set condtions for math problems 

#Restart/try again 

wn.listen()
wn.mainloop()