#Hurdles race
# Reeborg has entered a hurdle race, but he does not know in advance how long the race is. 
# Make him run the course, following a path similar to the one shown, 
# but stopping at the only flag that will be shown after the race has started.
# What you need to know
# The functions move() and turn_left().
# The condition at_goal() and its negation.
# How to use a while loop.



#creating the function for Reeborg to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#creating the function for Reeborg to ran and jump
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#while loop to make Reeborg stop at the flag
while at_goal() == False:
    jump()