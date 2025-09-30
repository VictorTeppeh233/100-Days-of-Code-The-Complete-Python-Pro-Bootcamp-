# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#initialize highest at 0
highest_score = 0

#create a for loop that updates highest if i is greater than it
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")