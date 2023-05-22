import random

print("Welcome to the Number Guessing game \nPlease choose number between 1 to 10")


computer_number = random.randint(1, 10)
a = True
while a:
    print(computer_number)
    user_number = int(input("Please chose number: "))
    if user_number > 10:
        print("please guess number between 1 to 10")
    elif user_number == computer_number:
        print("Congratulation, You won!")
        a = False
    elif user_number > computer_number:
        print("Wrong answer. Guess a bit lower number")
    else:
        print("Wrong answer. Guess a bit higher number")