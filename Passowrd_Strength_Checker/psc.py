import re

def min_length_check(user_input):
    if len(user_input) < 8:
        print("your password is too weak/ must be 8 charachters or longer.")
        return
    
def 
    if not re.search(r"\d", user_input):
        print("Your password is too weak/ does not contain numbers must contain numbers.")
        return
        

    pattern = r'[^\w\s]' 

    if not re.search(pattern, user_input):
        print("Your password is to weak/ does not contain symbol must contain characters.")
        return

    if not any(upper_case.isupper() for upper_case in user_input):
        print("Your password is too weak/ does not contain upper case letter. you need atleast one upper case")

    if not any(upper_case.islower() for upper_case in user_input):
        print("Your password is too weak/ does not contain lower case letter. you need atleast one lower case")

def main():
    while True:
        user_input = input("Enter your password: ")

        min_length_check(user_input)

        if  user_input == 'n':
            break

main()