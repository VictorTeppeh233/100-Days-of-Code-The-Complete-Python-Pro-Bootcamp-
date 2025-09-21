# Bmi Calculator

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# change values to float so you can take decimal values
height = float(height)
weight = float(weight)

# perform calculations
bmi = weight / height**2

# convert it to integer
bmi = int(bmi)

# print the answer
print(bmi)









