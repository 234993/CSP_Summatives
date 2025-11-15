import turtle as trtl 
import random as rand
import leaderboard
def setup():
    global score_writer, square, plus, divide, times, minus, player_right, number_one_e, number_two_e
    global player_answer, number_list1, number_list2, number_list1_e, number_list2_e
    global animal_random, animal, player_name, character, wn, player, number_one, number_two, score
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
    animal = trtl.Turtle()
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

    wn.addshape("unicorn.gif")
    wn.addshape("dragon.gif")
    wn.addshape("phoenix.gif")
    wn.addshape("nine_tails.gif")

    animal.hideturtle()
    animal.penup()
    animal.goto(-325, 325)

    #set condtions for layout 
    square.penup()
    divide.hideturtle()
    plus.hideturtle()
    minus.hideturtle()
    times.hideturtle()
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
    number_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    number_list1_e = [ 10, 12, 16, 18, 20]
    number_list2_e = [2]

    animal_list = ("unicorn.gif", "dragon.gif", "phoenix.gif", "nine_tails.gif")
    animal_random = rand.choice(animal_list)

    number_one_e = rand.choice(number_list1_e)
    number_two_e = rand.choice(number_list2_e)

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=("Arial", 24, "bold" ))

# change background 

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





def random_pick():
 global number_one, number_two
 number_one = rand.choice(number_list1)
 number_two = rand.choice(number_list2)








def question_one():
        global number_one, number_two 
        random_pick()
        player_answer = trtl.textinput("Question 1", "What is " + str(number_one) + " + " + str(number_two))
        if player_answer == str(number_one + number_two): # when the answer is correct move on and move the charactors position up 
            update_score()
            player_right.clear()
            player_right.write("Good Job! " + player_name + " Pick a Hop scotch spot to move forward!", align="center", font=("Arial", 24, "bold"))
            player_right.hideturtle()
        else: 
            player_right.clear()   
            player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))
            lost_restart()
            player_answer = trtl.textinput("Question 1", "What is " + str(number_one) + " + " + str(number_two))
            

def question_two_pick():
    global number_one, number_two 
    random_pick()
    player_answer2 = trtl.textinput("Moving on, ", "Would you like to move on to minus or plus equation? (m or p)" ) # ask the player if they want to do a plus or minus equation  
    if player_answer2 == "m":
        character.goto(-100, -225)
        character.stamp()
        player_answer2 = trtl.textinput("Question 2", "What is " + str(number_one) + " - " + str(number_two))
        if player_answer2 == str(number_one - number_two):
            update_score()
            player_right.clear()
            player_right.write("Good Job! " + player_name + " Move one Hop Scotch up", align="center", font=("Arial", 24, "bold"))
            player_right.hideturtle()
            character.goto(0, -25)
            character.stamp()
        else:
            player_right.clear()
            player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))
            player_right.hideturtle()
            lost_restart()
            
    else:
        character.goto(100, -225)#why is this not working 
        character.stamp()
        player_answer = trtl.textinput("Question 2", "What is " + str(number_one) + " + " + str(number_two))
        if player_answer == str(number_one + number_two):
            update_score()
            player_right.clear()
            player_right.write("Good Job! " + player_name + "Move one Hop Scotch up", align="center", font=("Arial", 24, "bold"))
            player_right.hideturtle()
            character.goto(0, 25)
            character.stamp()
        else: 
            player_right.clear()   
            player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))
            lost_restart()
            


def question_three():
        global number_one, number_two 
        random_pick()
        player_answer = trtl.textinput("Question 3", "What is " + str(number_one) + " * " + str(number_two))
        if player_answer == str(number_one * number_two):
            update_score()
            player_right.clear()
            player_right.write("Good Job! " + player_name + " Move one Hop scotch up!", align="center", font=("Arial", 24, "bold"))
            player_right.hideturtle()
        else:
            player_right.clear()
            player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))
            lost_restart()
            player_right.hideturtle()
            player_answer = trtl.textinput("Question 3", "What is " + str(number_one) + "* " + str(number_two))
            



def question_four_pick():
    global number_two_e, number_one_e
    player_answer2 = trtl.textinput("Moving on, ", "Would you like to move on to divide or minus equation? (d or m)" ) # ask the player if they want to do a plus or minus equation  
    if player_answer2 == "d":
        character.goto(-100, 175)
        character.stamp()
        player_answer2 = trtl.textinput("Question 2", "What is " + str(number_one_e) + " / " + str(number_two_e))
        if player_answer2 == str(number_one_e // number_two_e):
            update_score()
            player_right.clear()
            player_right.write("Good Job! " + player_name + " Move one Hop Scotch up", align="center", font=("Arial", 24, "bold"))
            player_right.hideturtle()
            character.goto(0, 375)
            character.stamp()
        else:
            player_right.clear()
            player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))
            lost_restart()
            player_right.hideturtle()
            
    else:
        character.goto(100, 175)#why is this not working 
        character.stamp()
        player_answer = trtl.textinput("Question 2", "What is " + str(number_one) + " - " + str(number_two))
        if player_answer == str(number_one - number_two):
            update_score()
            player_right.clear()
            player_right.write("Good Job! " + player_name + " Move one Hop Scotch up", align="center", font=("Arial", 24, "bold"))
            player_right.hideturtle()
            character.goto(0, 375)
            character.stamp()

        else: 
            player_right.clear()   
            player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))
            lost_restart()

def question_five():
    global number_one, number_two 
    random_pick()
    player_answer = trtl.textinput("Question 5", "What is " + str(number_one) + " + " + str(number_two))
    if player_answer == str(number_one + number_two): # when the answer is correct move on and move the charactors position up 
            update_score()
            player_right.clear()
            player_right.write("Good Job! " + player_name + " Pick a Hop scotch spot to move forward!", align="center", font=("Arial", 24, "bold"))
            player_right.hideturtle()
    else: 
            player_right.clear()   
            player_right.write("Try Again! " + player_name, align="center", font=("Arial", 24, "bold"))
            lost_restart()
            


def random_prize():
     if score == 5:
          player_right.clear()
          player_right.write("Great Job! Here is your prize! " + player_name, align="center", font=("Arial", 24, "bold"))
          animal.showturtle()
          animal.shape(animal_random)

def lost_restart():
    global player_answer
    player_answer = trtl.textinput("Lost ","You lost would you like to try again! " + player_name + " y or n ")
    if player_answer == "y":
        wn.clear()
        setup()
    else:
        wn.bye()
     

  
setup()    
random_pick()
question_one()
question_two_pick()
question_three()
question_four_pick()
question_five()
random_prize()

       
 


wn.listen()
wn.mainloop()