import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""
#Easy Level 
password= ""
for i in range(0,nr_letters):
    password=password + random.choice(letters)

for i in range(0,nr_numbers):
    password=password + random.choice(numbers)

for i in range(0,nr_symbols):
    password=password + random.choice(symbols)

print(password)
"""
#Hard Level
password_list=[]

for i in range(0,nr_letters):
    password_list.append(random.choice(letters))

for i in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

for i in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

print(password_list)

random.shuffle(password_list)
password=""
for i in range(0,nr_letters+nr_numbers+nr_symbols):
    password=password+ password_list[i]

print("Password is ",password)
