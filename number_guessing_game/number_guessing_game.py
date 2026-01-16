import random

def guessing_game(secret_number):

    counter = 0   # variable to hold number of tries

    while True:
        counter += 1

        user_input = input("Enter Number: ")
        
        if not user_input.isdigit():                  # clause to validate user input
            print("Number not valid. Please enter a valid number.")
            continue

        guessed_number = int(user_input)

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
    try_again = str(input("Do you want to Play Again? (Y/N): ")) # asking for replay

    answer = try_again.lower()

    if answer != "y":
        break


