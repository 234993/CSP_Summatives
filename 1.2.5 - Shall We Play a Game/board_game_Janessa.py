#todo players turtles 
import turtle as trtl

player_one = trtl.Turtle()
player_two = trtl.Turtle()

player_one_avatar = ("blue_ship.gif")
player_two_avatar = ("red_ship.gif")

#todo window start screen 
wn = trtl.Screen()
wn.bgpic("pirates_board_game_backg.gif")
wn.addshape(player_one_avatar)
wn.addshape(player_two_avatar)

#todo players movement 
player_one.penup()
player_two.penup()
player_one.goto(-100,100)
player_two.goto(-100,100)
player_one.pendown()
player_two.pendown()

# dice button 




# dice number appering on the screen(in the chest)



# How to reconize when the game is won 





# option to end or restart the game 


wn.mainloop()