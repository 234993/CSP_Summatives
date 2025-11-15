#todo players turtles 
import turtle as trtl
import random as rand #lets me roll dice
import time  


#Turtles created-------------------------------------------------------------------
player_one = trtl.Turtle() #create players as turtles so they can move
player_two = trtl.Turtle()
wn = trtl.Screen()
wn.tracer(0)
button = trtl.Turtle() #create to push button 
button_2 = trtl.Turtle()
rolled_number = trtl.Turtle() 
player_1_score = trtl.Turtle()
player_2_score = trtl.Turtle()
player_win = trtl.Turtle()
warning_message = trtl.Turtle()

#make the screen bigger 
wn.setup(width=1500, height=1000) 

#make the game setup together with a def 
def setup():
    global time, player_one, player_two, button, button_2, rolled_number
    global player_1_score, player_2_score, player_win
    global warning_message, position_1_p1, position_1_p2, player_show_score, player2_show_score



    #add images over the turtles-------------------------------------------------------------------------------------

    player_one_avatar = ("blue_ship.gif") 
    player_two_avatar = ("red_ship.gif")
    button_clicker_1 = ("button.gif")
    button_clicker_2 = ("button.gif")

    #todo window start screen 
    wn.bgpic("pirates_board_game_backg.gif") # background to base movments on 

    #add images as shapes 
    wn.addshape(player_one_avatar) #add images to the program  
    wn.addshape(player_two_avatar) 
    wn.addshape(button_clicker_1) #add a cover that says button 
    wn.addshape(button_clicker_2) #add a cover that says button 

    #players 
    player_one.shape("blue_ship.gif")#add images over my turtles
    player_two.shape("red_ship.gif")

    #buttons 
    button.shape("button.gif")
    button_2.shape("button.gif")

    #todo players start movement-----------------------------------------------------------------------------------------------
    
    wn.update() #makes sure to appers on the screen 
    #player one
    player_one.penup()
    player_one.goto(-600,345)# opposite sides of the board at the start squares 
    player_one.pendown()
    player_one.setheading(0)
    #player two 
    player_two.penup()
    player_two.goto(530,-335)
    player_two.pendown()
    player_two.setheading(180)

    #the number on the screen moved to the chest 
    rolled_number.penup()
    rolled_number.hideturtle()
    rolled_number.goto(100,100)

    #button one 
    button.hideturtle()
    button.penup()
    button.goto(650,350)
    button.showturtle()
    #button two 
    button_2.hideturtle()
    button_2.penup()
    button_2.goto(650,-350)
    button_2.showturtle()

    #player ones score 
    player_1_score.hideturtle()
    player_1_score.penup()
    player_1_score.goto(-670,360) 

    # player two score
    player_2_score.hideturtle()
    player_2_score.penup()
    player_2_score.goto(530,-405) 

    # player one dislplay if win 
    player_win.hideturtle()
    player_win.penup()
    player_win.goto(0,0) 

    # Warning message in the begining 
    warning_message.hideturtle()
    warning_message.penup()
    warning_message.goto(-500,0)

#end of setup
setup()
position_1_p1 = 0
position_1_p2 = 0
# player ones and twos scores
player_show_score = 0 
player2_show_score =0
def clear():
    global position_1_p1, position_1_p2, player2_show_score, player_show_score
    position_1_p1 = 0
    position_1_p2 = 0
    # player ones and twos scores
    player_show_score = 0 
    player2_show_score =0
    player_one.clear()
    player_two.clear()
    rolled_number.clear()
    player_1_score.clear()
    player_2_score.clear()
    player_win.clear()
    warning_message.clear()
    player_one.showturtle()
    player_two.showturtle()

# effects of landing on certain spaces for player one 
p1_consequence_1 = [8,19,27]
p1_consequence_3 = [4,23]
p1_boost = [13,29]

# effects of landing on certain spaces for player two 
p2_consequence_1 = [3,11,24]
p2_consequence_3 =[7,20]
p2_boost = [13,29]


#update screen
wn.update()
wn.tracer(True)


#dummy function so the user cannot double roll

def dummy(x,y):
    print("What for movment to complete")
# dice number appering on the screen(in the chest) + #todo have the players move and take turns-------------------------------------------------
def roll_dice_1(x,y): #same as roll_dice_2
    global button, position_1_p1, player_1_score, player_show_score
    button.onclick(dummy)
    button_pushed = rand.randint(1,5) #had to make out of 7 becuase thats the shortest part of the board
    rolled_number.goto(-50,30) 
    rolled_number.write(button_pushed, font=("Arial", 30, "normal")) #found in the leaderboard code
    player_one.penup()
    for i in range(button_pushed):
        if position_1_p1 == 32:
            position_1_p1 = 0 #resets back to start value
            player_show_score +=1
            player_1_score.write(player_show_score, font=("Arial", 30, "normal"))
            time.sleep(0.5)
            if player_show_score == 3:#how to reconize when someone won 
                player_name = "player one"
                player_win.write(player_name + " wins!!!!!", font=("Arial", 40, "normal"))
                player_one.goto(-450,200)
                player_one.stamp()
                player_two.hideturtle()
                look_winner(player_name, player_win)
            if player_show_score == 2:
                player_one.goto(-350,150)
                player_one.stamp()
            if player_show_score == 1:
                player_one.goto(-250,80)
                player_one.stamp()
            player_one.goto(-600,345)
            player_one.setheading(360)
            player_1_score.clear()
        if position_1_p1 == 10: 
            player_one.setheading(270)
        if position_1_p1 == 16:
            player_one.setheading(180)
        if position_1_p1 == 26:
            player_one.setheading(90)
        player_one.forward(110) 
        position_1_p1 +=1
        rolled_number.clear()#stop the numbers from overlapping 
    if position_1_p1 in p1_consequence_3:
        player_one.backward(110 * 3)
        position_1_p1 -= 3
    if position_1_p1 in p1_consequence_1:
        player_one.backward(110)
        position_1_p1 -= 1
    if position_1_p1 in p1_boost:
        player_one.forward(110)
        position_1_p1 +=1 
    button.onclick(roll_dice_1)    
  
button.onclick(roll_dice_1)

def look_winner(player_name, player_win):
    player_win.write(player_name + " wins!!!!!", font=("Arial", 40, "normal"))
    restrat_game = trtl.textinput("Restart Game:", "Would you like to restart the game?") # use this to ask about restarting the game 
    if restrat_game == "yes":
        clear()
        setup()
        player_one.penup()
        player_two.penup()
        #working on it 
    else:
        wn.bye()
# player twos section------------------------------------------------------------------------------------------------------------
dummy
def roll_dice_2(x,y):# can i use x and y because it kinda dose noting but act as a place holder
    global button_2, player2_show_score, position_1_p2
    button_2.onclick(dummy) 
    button_2_pushed = rand.randint(1,5) #had to make out of 7 becuase thats the shortest part of the board
    rolled_number.goto(-50,30) 
    rolled_number.write(button_2_pushed, font=("Arial", 30, "normal")) #found in the leaderboard code
    player_two.penup()
    for x in range(button_2_pushed):
        if position_1_p2  == 32:
            position_1_p2 = 0 #resets back to start value
            player_two.setheading(180)
            player2_show_score +=1
            player_2_score.write(player2_show_score, font=("Arial", 30, "normal"))
            time.sleep(0.5)
            if player2_show_score == 3: #how to reconize when someone won 
                player_name = "player two "
                player_win.write(player_name + " wins!!!!!", font=("Arial", 40, "normal"))
                player_two.goto(150,-50)
                player_two.stamp()
                player_one.hideturtle()
                look_winner(player_name, player_win)
            if player2_show_score == 2:
                player_two.goto(250,-130)
                player_two.stamp()
            if player2_show_score == 1:
                player_two.goto(375,-180)
                player_two.stamp()
            player_two.goto(530,-335)
            player_two.setheading(180)
            player_2_score.clear()
        if position_1_p2 == 10: 
            player_two.setheading(90)
        if position_1_p2 == 16:
            player_two.setheading(0)
        if position_1_p2 == 26:
            player_two.setheading(270)
        player_two.forward(114) 
        position_1_p2 +=1
        rolled_number.clear()#stop the numbers from overlapping 
    if position_1_p2 in p2_consequence_1: 
      player_two.backward(114)
      position_1_p2 -= 1
    if position_1_p2 in p2_consequence_3:
        player_two.backward(114 * 3)
        position_1_p2 -= 3
    if position_1_p2 in p2_boost:# only need one of these 
        player_two.forward(110)
        position_1_p2 +=1
    button_2.onclick(roll_dice_2)

button_2.onclick(roll_dice_2)


# option to end or restart the game 


wn.mainloop()