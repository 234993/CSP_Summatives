import turtle as trtl 
import random as rand
import leaderboard_letter
global player_answer, number_one, number_two 
wn = trtl.Turtle()
wn.hideturtle()
wn = trtl.Screen()
square  = trtl.Turtle()
plus = trtl.Turtle()
times = trtl.Turtle()
minus = trtl.Turtle()
divide = trtl.Turtle()
character = trtl.Turtle()
player_right = trtl.Turtle()
score_writer = trtl.Turtle()
player_right.hideturtle()
player_right.penup()
player_right.goto(200,400)
player_right.color("brown")
character.penup()
plus.penup()
square.speed(0) #take out after testing 
#Ask player for name 
player_name = trtl.textinput("Name:", "Hello what is your name?")
player = trtl.textinput("Message",  player_name +", Are you ready to escape to the zoo?")
player = player.lower()
#------------------------------------------------------------------------------------------------------------------------------
#Leaderboard 
score_writer.hideturtle() 
score_writer.penup()
score_writer.goto(475,475)
score = 0

def update_score():
    global score 
    score += 1
    score_writer.clear()
    score_writer.write(score, font=("Arial", 24, "bold" ))

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

number_one = rand.choice(number_list1)
number_two = rand.choice(number_list2)

def question_one():
    for c in range(1):
        global character_p
        player_answer = trtl.textinput("Question 1", "What is " + str(number_one) + " + " + str(number_two))
        if player_answer == str(number_one + number_two): # when the answer is correct move on and move the charactors position up 
            update_score()
            player_right.clear()
            player_right.write("Good Job! " + player_name + " Pick a Hop scotch spot to move forward!", align="center", font=("Arial", 24, "bold"))
            character_p += 1
            player_right.hideturtle()
        else: 
            player_right.clear()   
            player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))

def question_two_pick():
   player_answer = trtl.textinput("Moving on, ", "Would you like to move on to minus or plus equation? (m or p)" ) # ask the player if they want to do a plus or minus equation  
   for c in range(1):
       global character_p
       if player_answer == "m":
        character.goto(-100, -225)
        character.stamp()
        player_answer = trtl.textinput("Question 2", "What is " + str(number_one) + " - " + str(number_two))
        if player_answer == "p":
            character.goto(100, -225)#why is this not working 
            character.stamp()
            player_answer = trtl.textinput("Question 2", "What is " + str(number_one) + " + " + str(number_two))
            if player_answer == str(number_one - number_two):
             update_score()
             character_p += 1
             player_right.write("Good Job! " + player_name + "Move one Hop Scotch up", align="center", font=("Arial", 24, "bold"))
            elif player_answer == str(number_one + number_two):
                update_score()
                character_p += 1
                player_right.write("Good Job! " + player_name + "Move one Hop Scotch up", align="center", font=("Arial", 24, "bold"))
            else: 
              player_right.clear()   
              player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))

def question_two():
    for c in range(1):
        global character_p
        player_answer = trtl.textinput("Question 2", "What is " + str(number_one) + " + " + str(number_two))
        if player_answer == str(number_one + number_two):
            update_score()
            character_p += 1
            player_right.write("Good Job! " + player_name + " Move one Hop scotch up!", align="center", font=("Arial", 24, "bold"))
            character.goto(0, -25)
            character.stamp()
        else:  
            player_right.clear()   
            player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))

def question_three():
    for c in range(1):
        global character_p
        player_answer = trtl.textinput("Question 3", "What is " + str(number_one) + "* " + str(number_two))
        if player_answer == str(number_one * number_two):
            update_score
            character_p += 1
            player_right.write("Good Job! " + player_name + " Move one Hop scotch up!", align="center", font=("Arial", 24, "bold"))
        else:
            player_right.clear()
            player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))

question_one()
question_two_pick()
question_two()
question_three()

       
 


wn.listen()
wn.mainloop()