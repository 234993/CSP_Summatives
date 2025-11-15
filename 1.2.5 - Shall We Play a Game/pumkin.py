import turtle as trtl

# Create screen
screen = trtl.Screen()

# Ask user for shape
shape = screen.textinput("Pumpkin Shape", "What shape for the pumpkin? (oval, circle): ")

# Handle cancel or empty input
'''if shape:
    shape = shape.lower()
else:
    shape = "circle"  # default
    '''

# Setup turtle
trtl.speed(0)
trtl.penup()
trtl.goto(-200, -100)
trtl.pendown()

# Draw pumpkin
if shape == "circle":
    trtl.circle(100)
elif shape == "oval":
    for i in range(2):
        trtl.circle(100, 90)
        trtl.circle(50, 90)
else:
    trtl.circle(100)  # fallback

# Keep window open
trtl.done()