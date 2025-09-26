# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

#adding the names together
name_total = name1 + name2

#counting for true
t = name_total.count("t")
r = name_total.count("r")
u = name_total.count("u")
e1 = name_total.count("e")

#calculating for true
true = t + r + u + e1

#counting for love
l = name_total.count("l")
o = name_total.count("o")
v = name_total.count("v")
e2 = name_total.count("e")

#calculating for love
love = l + o + v + e2

#converting them to strings
true = str(true)

love = str(love)

#adding the strings
check = true + love

#converting the added strings to integer
check = int(check)

#if statements to print the message
if (check < 10) or (check > 90):
    print(f"Your score is {check}, you go together like coke and mentos.")
elif (check > 40) and (check < 50):
    print(f"Your score is {check} you are alright together")
else:
    print(f"Your score is {check}.")