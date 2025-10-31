#todo players turtles 
import turtle as trtl
import random as rand #lets me roll dice
global time 
import time  
global player_one 




#Turtles created-------------------------------------------------------------------
player_one = trtl.Turtle() #create players as turtles so they can move
player_two = trtl.Turtle()
wn = trtl.Screen()
button = trtl.Turtle() #create to push button 
button_2 = trtl.Turtle()
rolled_number = trtl.Turtle() #had to create 
player_1_score = trtl.Turtle()

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
player_1_score.showturtle()

#Todo try target points----------------------------------------------------------------------------------------------------------------------
position_1_p1 = 0
position_1_p2 = 0
p1_consequence_1 = [8,19,27]
p1_consequence_3 = [4,23]
p2_consequence_1 = [3,7,11,20,24]
p1_boost = [13,29]
p2_boost = [13,29]

#todo recoding the scroce 
fist_step_stamp1 = (-600,345)
player_1_score_display = 0
player_2_score = 0
# dice number appering on the screen(in the chest) + #todo have the players move and take turns 
def roll_dice_1(x,y): #used x and y becuase i needed some sort of 2 arguments in the def 
    global position_1_p1
    global player_1_score_display
    button_pushed = rand.randint(1,5) #had to make out of 7 becuase thats the shortest part of the board
    rolled_number.goto(-50,30) 
    rolled_number.write(button_pushed, font=("Arial", 30, "normal")) #found in the leaderboard code
    player_one.penup()
    for i in range(button_pushed):
        if position_1_p1 == 32:
            position_1_p1 = 0 #resets back to start value
            player_one.goto(-250,80)
            player_one.stamp()
            player_one.goto(-600,345)
            player_one.setheading(360)
            player_1_score_display += 1
            player_1_score.write("Player 1 score =", player_1_score_display, font=("Arial", 30, "normal"))
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
  
            
#liat of spaces that set you back or forward/number spaces different for the dif avatars 
   
button.onclick(roll_dice_1)

def roll_dice_2(x,y):
    global position_1_p2  
    button_2 = rand.randint(1,5) #had to make out of 7 becuase thats the shortest part of the board
    rolled_number.goto(-50,30) 
    rolled_number.write(button_2, font=("Arial", 30, "normal")) #found in the leaderboard code
    player_two.penup()
    for x in range(button_2):
        if position_1_p2  == 32:
            position_1_p2 = 0 #resets back to start value
            player_two.setheading(180)
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
    if position_1_p2 in p2_boost:
        player_two.forward(110)
        position_1_p2 +=1 
  

button_2.onclick(roll_dice_2)





# How to reconize when the game is won 





# option to end or restart the game 


wn.mainloop()