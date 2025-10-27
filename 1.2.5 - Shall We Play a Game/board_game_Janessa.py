#todo players turtles 
import turtle as trtl
import random as rand #lets me roll dice 
player_one = trtl.Turtle() #create players as turtles so they can move
player_two = trtl.Turtle()

player_one_avatar = ("blue_ship.gif") 
player_two_avatar = ("red_ship.gif")
button_clicker = ("button.gif")
#todo window start screen 
wn = trtl.Screen()
wn.bgpic("pirates_board_game_backg.gif") # background to base movments on 
wn.addshape(player_one_avatar) #add images to the program  
wn.addshape(player_two_avatar) 
wn.addshape(button_clicker) #add a cover that says button 

#todo players movement 
wn.update() #makes sure to appers on the screen 
player_one.shape("blue_ship.gif")#add images over my turtles
player_two.shape("red_ship.gif")
player_one.penup()
player_two.penup()
player_one.goto(-600,345)# opposite sides of the board at the start squares 
player_two.goto(540,-335)
player_one.pendown()
player_two.pendown()

# dice button- use a turtle to do this 
button = trtl.Turtle() #create to push button 
rolled_number = trtl.Turtle() #had to create 
rolled_number.goto(100,100)
button.hideturtle()
button.shape("button.gif")
button.penup()
button.goto(650,350)
button.showturtle()
def roll_dice(x,y): #used x and y becuase i needed some sort of 2 arguments in the def 
    button_pushed = rand.randint(1,12)
    rolled_number.write(button_pushed, font=("Arial", 30, "normal")) #found in the leaderboard code 
    
button.onclick(roll_dice)



# dice number appering on the screen(in the chest)


# How to reconize when the game is won 





# option to end or restart the game 


wn.mainloop()