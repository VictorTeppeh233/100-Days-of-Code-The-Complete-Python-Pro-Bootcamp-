# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#intializing the variables to 0
total = 0
number = 0

#using the for loop
for i in student_heights:
  total += i
  number += 1

#calculating the average height
average = (total / number)

#rounding it
average = round(average)

#printing the height
print(average)