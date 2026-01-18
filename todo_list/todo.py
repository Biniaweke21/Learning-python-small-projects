todo_list = []

def todo_func(menu_choice, todo_list):
    if menu_choice== 1:
        added_task = input("Write the task you want to add: ")
        todo_list.append(added_task)

        print(f"You have added {added_task} to your list, Thankyou")
    elif menu_choice == 2:
        print(todo_list)
    else:
        print("you chose to mark task as done")
     
        

while True:
    
    user_input = input("""
    ---------Menu---------
        1,Add Task
        2,View Task
        3,Mark Task as Done
        4,exit
            Choice: """)

    if  not user_input.isdigit():
        print("Please Enter a Valid Number")
        continue

    menu_choice = int(user_input)
    

    if menu_choice > 4 or menu_choice < 1:
        print("Please Enter a valid Number")
        continue
    elif not menu_choice==4:
        todo_func(menu_choice, todo_list)
    else:
        break

