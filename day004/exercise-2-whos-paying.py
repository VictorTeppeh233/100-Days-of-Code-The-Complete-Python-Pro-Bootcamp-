# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#importing random module
import random

#getting the last index of names
l = int(len(names)) - 1

#generating a random index of the names
randomness = random.randint(0, l)

#displaying the random name
print(f"{names[randomness]} is going to buy the meal today!")

