# Data Types
# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# assigned the first and second numbers to variables
num_1 = two_digit_number[0]

num_2 = two_digit_number[1]

# converted the numbers to integers since input takes in strings by default
num_1 = int(num_1)
num_2 = int(num_2)

# add the integers
print(num_1 + num_2)