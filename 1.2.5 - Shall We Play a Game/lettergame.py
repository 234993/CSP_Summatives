import turtle as trtl 
import random as rand
import leaderboard_letter
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
leaderboard_file = "leader_file.txt"
leaderboard_names = []
leaderboard_scores = []
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
#start movmment -----------------------------------------------------------------------------------------------------------------------------------------------------------
    for c in range(1):# their are five steps on the hop scotch 
        number_one = rand.choice(number_list1)# pulling random numbers from this list 
        number_two = rand.choice(number_list2)
# start of question one-------------------------------------------------------------------------------------------------------------------------------------------------
        if character_p == 0: # if the charactor is in spot one ask a the fist qurstion 
            player_answer = trtl.textinput("Question 1", "What is " + str(number_one) + " + " + str(number_two))
            if player_answer == str(number_one + number_two): # when the answer is correct move on and move the charactors position up 
                update_score()
                player_right.showturtle()
                player_right.write("Good Job! " + player_name + " Pick a Hop scotch spot to move forward!", align="center", font=("Arial", 24, "bold"))
                player_right.hideturtle()
                player_answer = trtl.textinput("Moving on, ", "Would you like to move on to minus or plus equation? (m or p)" ) # ask the player if they want to do a plus or minus equation 
            else:        
                player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))
                player_right.hideturtle()
                player_answer = trtl.textinput("Question 1", "What is " + str(number_one) + " + " + str(number_two))
                player_answer = trtl.textinput("Moving on, ", "Would you like to move on to minus or plus equation? (m or p)" )
#Start of question two------------------------------------------------------------------------------------------------------------------------------------------
                if player_answer == "m": # if they answer minus move the charactor to that spot 
                        character.goto(-100, -225)
                        character.stamp()
                        player_answer = trtl.textinput("Question 2", "What is " + str(number_one) + " - " + str(number_two))
                        if player_answer == str(number_one - number_two): # if the answer is right move forward 
                            update_score()
                            player_right.clear()
                            player_right.write("Good Job! " + player_name + " Pick a Hop scotch spot to move forward!", align="center", font=("Arial", 24, "bold"))
                            player_right.hideturtle()
                        else:
                                player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))
                                player_right.hideturtle()
                                
                else:
                    character.goto(100, -225)
                    character.stamp()
                    player_answer = trtl.textinput("Question 2", "What is " + str(number_one) + " + " + str(number_two))
                    if player_answer == str(number_one + number_two):
                        update_score()
                        player_right.clear()  
                        player_right.write("Good Job! " + player_name + " Pick a Hop scotch spot to move forward!", align="center", font=("Arial", 24, "bold"))  
                        character_p == 3
                        print("done3")
                    else:
                        player_right.clear()
                        player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold")) 
                   
#start of question 3---------------------------------------------------------------------------------------------------------------------------------------------------------
        










#Restart/try again 

wn.listen()
wn.mainloop()