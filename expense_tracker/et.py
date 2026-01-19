def add_expense(expense_list, total_expense):

    while True:
        expense_name = input("Enter expense Name: ")
        user_value = input("Enter expense Value: ")
        print(" ")

        if not user_value.isdigit():
            print("""The expense value needs to be a number: 
                  """)
            continue
        

        expense_value = int(user_value)

        if expense_value <= 0:
            print("""The expense should be greater than 0: 
                  """)
            continue

        total_expense += expense_value

        expense_list.append([expense_name, expense_value])

        print(f"""Added: Expense Name: {expense_name},       
       Expense Value: {expense_value}""")
        return total_expense
    

def view_all(expense_list):

    if not expense_list:
        print("There is no expenses to show")
        return

    for index, item in enumerate(expense_list, start=1):
        print(f"Expense {index}: {item[0]} , {item[1]}")



def view_total(expense_list, total_expense):    
    
    if not expense_list:
        print("There is no expenses to show")
        return
    
    print(f"Your total expense is: {total_expense}")


def menu_choice_handler(user_choice, expense_list, total_expense):

    if user_choice == 1:
        total_expense= add_expense(expense_list, total_expense)
    elif user_choice == 2:
        view_all(expense_list)
    elif user_choice == 3:
        view_total(expense_list, total_expense)

    return total_expense




def main():


    expense_list = []

    total_expense = 0

    while True:
        user_input = input("""
    --------Menu--------
        1. Add Expense  
        2. View all Expenses
        3. View total Expenses
        4. Exit      
        
        Choice:""")
        
        if not user_input.isdigit():
            print("please enter a number.")
            continue

        user_choice = int(user_input)

        if user_choice < 1 or user_choice > 4:
            print("Enter the correct number choice: ")
            continue
        if user_choice == 4:
            break

        total_expense = menu_choice_handler(user_choice, expense_list, total_expense)

main()