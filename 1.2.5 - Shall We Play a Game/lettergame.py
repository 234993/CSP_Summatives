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
character = trtl.Turtle()
character.penup()
plus.penup()
#Ask player for name 
player = trtl.textinput("Name:", "Hello what is your name?")
player = trtl.textinput("Message",  player +", Are you ready to escape to the zoo?")
player = player.lower()


#display message with captured name 



# change background 
wn.addshape("character.gif")
character.penup()
character.shape("character.gif")

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
    square.goto(0, -425)
    square.color(rand.choice(square_list_color))
    square.stamp()
    square.goto(100, -225)
    square.color(rand.choice(square_list_color))
    square.stamp()
    square.goto(-100, -225)
    square.color(rand.choice(square_list_color))
    square.stamp()
    square.goto(0, -25)
    square.color(rand.choice(square_list_color))
    square.stamp()
    square.goto(-100, 175)
    square.color(rand.choice(square_list_color))
    square.stamp()
    square.goto(100, 175)
    square.color(rand.choice(square_list_color))
    square.stamp()
    square.goto(0, 375)
    square.color(rand.choice(square_list_color))
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

character_p = 0
number_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if player == "n":
    wn.bye()
else:
    wn.bgpic("background.gif")
    place()
    symbol_set_up()
    divide.showturtle()
    plus.showturtle()
    minus.showturtle()
    times.showturtle()
    character.goto(0, -425)
    character.stamp()
    for c in range(5):
        if character_p == 0:
            player = trtl.textinput("Question 1", "What is " + str(rand.choice(number_list1)) + " + " + str(rand.choice(number_list2)))
            if sum(number_list1 + number_list2) == True:
                break
            else:
                print("try again!")



#number list 




#Leaderboard 




#Timer/timer limt for each problem  



#Set condtions for math problems 

#Restart/try again 

wn.listen()
wn.mainloop()