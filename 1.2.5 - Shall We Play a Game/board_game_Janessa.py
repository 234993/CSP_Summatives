#todo players turtles 
import turtle as trtl

player_one = trtl.Turtle()
player_two = trtl.Turtle()

player_one_avatar = ("blue_ship.gif")
player_two_avatar = ("red_ship.gif")
button_clicker = ("button.gif")
#todo window start screen 
wn = trtl.Screen()
wn.bgpic("pirates_board_game_backg.gif")
wn.addshape(player_one_avatar)
wn.addshape(player_two_avatar)
wn.addshape(button_clicker)

#todo players movement 
wn.update()
player_one.shape("blue_ship.gif")
player_two.shape("red_ship.gif")
player_one.penup()
player_two.penup()
player_one.goto(-600,345)
player_two.goto(540,-335)
player_one.pendown()
player_two.pendown()

# dice button- use a turtle to do this 
button = trtl .Turtle()
button.shape("button.gif")
button.penup()
button.hideturtle()
button.goto(650,350)
button.showturtle()

# dice number appering on the screen(in the chest)



# How to reconize when the game is won 





# option to end or restart the game 


wn.mainloop()