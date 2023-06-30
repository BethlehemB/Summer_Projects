import random

print("Welcome to B Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*._-+~?'


while True:
    number = input("How many passwords would you like to generate: ")
    if number.isdigit() and number > 0:
        break
    else:
        print("Please enter a number")
        continue

while True:
    length = input("How many characters would you like: ")
    if length.isdigit and int(length) > 0:
        break
    else:
        print("Please enter a number: ")
        continue

print("\n Here are some of the passwords we've generated! ")
for pwd in range (number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
