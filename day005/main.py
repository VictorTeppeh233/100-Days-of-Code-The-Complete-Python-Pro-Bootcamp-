#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters_random_range = random.randint(0, len(letters)-1)
numbers_random_range = random.randint(0, len(numbers)-1)
symbols_random_range = random.randint(0, len(symbols)-1)

#initializing variables for the loop
random_letter = 0
final_letter = str()

#loop for letters
for i in range(1, nr_letters + 1):
    letters_random_range = random.randint(0, len(letters)-1)
    random_letter = letters[letters_random_range]
    final_letter += random_letter


#initializing variables for the loop
random_symbol = 0
final_symbol = str()

#loop for symbols
for s in range(1, nr_symbols + 1):
    symbols_random_range = random.randint(0, len(symbols)-1)
    random_symbol = symbols[symbols_random_range]
    final_symbol += random_symbol


#initializing variables for the loop
random_number = 0
final_number = str()

#loop for numbers
for i in range(1, nr_numbers + 1):
    numbers_random_range = random.randint(0, len(numbers)-1)
    random_number = numbers[numbers_random_range]
    final_number += random_number


print(f"Here is your password: {final_letter}{final_symbol}{final_number}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = f"{final_letter}{final_symbol}{final_number}"

#turning the password which is a string into a list
list_passowrd = list(password)

#shuffling the list
random.shuffle(list_passowrd)

#joining the shuffled characters back into a string
random_password = ''.join(list_passowrd)


print(f"Here is your password: {random_password}")

