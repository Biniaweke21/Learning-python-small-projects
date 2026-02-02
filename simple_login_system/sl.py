def registration(pass_holder):
    while True:
        user_name = input("Enter a user name: ")
        password = input("Enter your password: ")

        if user_name in pass_holder:
            print("Username already exist")
            choice = input("Do you want to: \n" 
            "1, Try another UserName?\n " 
            "2, Go back to the main menu: ")
            choice1 = int(choice)
            if choice1 == 1:
                continue
            elif choice1 == 2:
                break
            else:
                print("Wrong choice going back to the main menu...")
                break
        else:
            pass_holder.update({user_name : password})
            print("Registration Successful Thankyou! ")
            break

def login(pass_holder):

    while True:
        user_name = input("Enter your username: ")
        password = input("Enter your password: ")


        if user_name in pass_holder:
            if password == pass_holder[user_name]:
                print(f"Login succesful! Welcome {user_name}")
                break
            else:
                print(f"Password for user {user_name} is not correct try again")
            continue
        else:
            print("Username not found.")
            continue        



def main():
    pass_holder = {}

    while True:
        user_input = input("""
    --------Menu--------
        1. Registration
        2. Login
        3. Exit   
        
        Choice:""")

        choice = int(user_input)

        if choice == 1:
            registration(pass_holder)
        elif choice == 2:
            login(pass_holder)
        else:
            break


main()