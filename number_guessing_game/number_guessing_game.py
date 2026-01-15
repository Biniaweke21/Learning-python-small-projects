import random

def guessing_game(secret_number):

    while True:

        guessed_number = int(input("Enter Number: "))

        if secret_number > guessed_number:
            print("Too low, guess higher: ")
            
        elif secret_number < guessed_number:
            print("Too high, guess lower: ")
            
        else:
            print("Yay, you found the number!")
            break


random_number = random.randint(1, 100)

guessing_game(random_number)

