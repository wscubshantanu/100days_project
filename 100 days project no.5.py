import random
letters = ['a','b','c','d','e','f']
number = ['0','1','2','3','4','5']
symbols =['!','#','%','$','*']

print("welcome to the pypasswords generator! ")
nr_letters = int(input("how many letters would you like to your password?\n"))
nr_symbols = int(input("how many symbols would you like?\n"))
nr_numbers = int(input("how many numbers would you like ?\n"))

#easy level
#password = ""
#for char in range(0,nr_letters):
#  password += random.choice(letters)
#
#for char in range(0,nr_symbols):
#  password += random.choice(letters)
#
#for char in range(0,nr_numbers):
#  password += random.choice(letters)
#
#print(password)
#
#hard level
passwords_list = []
for char in range(0,nr_letters):
    passwords_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    passwords_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    passwords_list.append(random.choice(number))

print(passwords_list)
random.shuffle(passwords_list)
print(passwords_list)

passwords = ""
for char in passwords_list:
    passwords += char

print(f"your password is: {passwords}")
