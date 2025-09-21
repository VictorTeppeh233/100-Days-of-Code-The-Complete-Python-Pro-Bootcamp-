# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# made age an integer data type
age = int(age)

# performing the calculations
year = 90 - age

days = year * 365

weeks = year * 52

months = year * 12

# printing the message

print(f"You have {days} days, {weeks} weeks and {months} months left")
