#todo players turtles 
import turtle as trtl
import random as rand #lets me roll dice 
player_one = trtl.Turtle() #create players as turtles so they can move
player_two = trtl.Turtle()

player_one_avatar = ("blue_ship.gif") 
player_two_avatar = ("red_ship.gif")
button_clicker_1 = ("button.gif")
button_clicker_2 = ("button.gif")
#todo window start screen 
wn = trtl.Screen()
wn.bgpic("pirates_board_game_backg.gif") # background to base movments on 
wn.addshape(player_one_avatar) #add images to the program  
wn.addshape(player_two_avatar) 
wn.addshape(button_clicker_1) #add a cover that says button 
wn.addshape(button_clicker_2) #add a cover that says button 

#todo players movement 
wn.update() #makes sure to appers on the screen 
player_one.shape("blue_ship.gif")#add images over my turtles
player_two.shape("red_ship.gif")
player_one.penup()
player_two.penup()
player_one.goto(-600,345)# opposite sides of the board at the start squares 
player_two.goto(530,-335)
player_one.pendown()
player_two.pendown()
player_two.setheading(180)

# dice button- use a turtle to do this 
button = trtl.Turtle() #create to push button 
button_2 = trtl.Turtle()
rolled_number = trtl.Turtle() #had to create 
rolled_number.penup()
rolled_number.hideturtle()
rolled_number.goto(100,100)
button.hideturtle()
button_2.hideturtle()
button.shape("button.gif")
button_2.shape("button.gif")
button.penup()
button_2.penup()
button.goto(650,350)
button_2.goto(650,-350)
button.showturtle()
button_2.showturtle()

# dice number appering on the screen(in the chest)
def roll_dice_1(x,y): #used x and y becuase i needed some sort of 2 arguments in the def 
    button_pushed = rand.randint(1,5) #had to make out of 7 becuase thats the shortest part of the board
    rolled_number.goto(-50,30) 
    rolled_number.write(button_pushed, font=("Arial", 30, "normal")) #found in the leaderboard code
    player_one.penup()
    player_one.forward(button_pushed * 110) 
    rolled_number.clear()#stop the numbers from overlapping 
button.onclick(roll_dice_1)

def roll_dice_2(x,y): #used x and y becuase i needed some sort of 2 arguments in the def 
    button_2_pushed = rand.randint(1,5) #had to make out of 7 becuase thats the shortest part of the board
    rolled_number.goto(-50,30) 
    rolled_number.write(button_2_pushed, font=("Arial", 30, "normal")) #found in the leaderboard code
    player_two.penup()
    player_two.forward(button_2_pushed * 115) 
    rolled_number.clear()#stop the numbers from overlapping 
button_2.onclick(roll_dice_2)
#todo have the players move and take turns 




# How to reconize when the game is won 





# option to end or restart the game 


wn.mainloop()