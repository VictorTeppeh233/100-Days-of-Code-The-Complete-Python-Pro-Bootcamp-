#Reeborg has entered a hurdle race.
#Make him run the course, following a path similar to the one shown.

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

#calling the function
for i in range(6):
    jump()