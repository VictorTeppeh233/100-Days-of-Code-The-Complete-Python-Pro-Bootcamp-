#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#print the welcome message
print("Welcome to the tip calculator.")

# take the bill, tip% and the number of people
bill = input("What was the total bill? ")

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

people = input("How many people to split the bill? ")

#format the percentage
percent = float(percentage) / 100 + 1

#calculate the tip for each person
tip = float(bill) / int(people) * float(percent)

#format the tip
pay = f"{tip:.2f}"

#print the tip
print(f"Each person should pay: ${pay}")
