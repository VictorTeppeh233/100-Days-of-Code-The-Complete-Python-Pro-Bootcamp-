rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#importing random module
import random

#asking user for input
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#displaying the input
if user == 0:
    user = rock
    print(rock)

if user == 1:
    user = paper
    print(paper)

if user == 2:
    user = scissors
    print(scissors)

#displaying the computer's choice
print("Computer Chose")

choice = random.randint(0, 3)
computer = "0"
if choice == 0:
    computer = rock

if choice == 1:
    computer = paper

if choice == 2:
    computer = scissors

if computer == rock:
    print(rock)

if computer == paper:
    print(paper)

if computer == scissors:
    print(scissors)

#assigning the messages
win = "You win"
lose = "You lose"
draw = "Draw"


#logic for who wins the game
if computer == rock and user == rock:
    print(draw)

elif computer == paper and user == paper:
    print(draw)

elif computer == scissors and user == scissors:
    print(draw)

elif user == rock and computer == scissors:
    print(win)

elif user == rock and computer == paper:
    print(lose)

elif user == scissors and computer == paper:
    print(win)

elif user == scissors and computer == rock:
    print(lose)

elif user == paper and computer == rock:
    print(win)

elif user == paper and computer == scissors:
    print(lose)