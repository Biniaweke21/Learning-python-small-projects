import random

def guessing_game(secret_number):

    counter = 0

    while True:
        counter += 1

        guessed_number = int(input("Enter Number: "))

        if secret_number > guessed_number:
            print("Too low, guess higher: ")
            
        elif secret_number < guessed_number:
            print("Too high, guess lower: ")
            
        else:
            print(f"Yay! you found the correct number! The number is {secret_number}")
            print(f"It took you {counter} tries to get it")
            break

            
while True:
    
    random_number = random.randint(1, 100)
    guessing_game(random_number)
    try_again = str(input("Do you want to Play Again? (Y/N): "))

    if try_again != "y":
        break


