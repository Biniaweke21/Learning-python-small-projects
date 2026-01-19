todo_list = []

def todo_func(menu_choice, todo_list):
    if menu_choice== 1:
        add_task(todo_list)
    elif menu_choice == 2:
        view_task(todo_list)
    else: 
        if not todo_list:
            print("Your to do lost is Empty. ")
            return
        else:
            mark_done_func(todo_list)

def add_task(todo_list):
    added_task = input("Write the task you want to add: ")
    todo_list.append(added_task)
    print(" ")
    print(f"You have added {added_task} to your list, Thankyou")
        
        
def view_task(todo_list):
    if not todo_list:
        print("Your todo list is empty: please add tasks")
        return
        
    print("Tasks you have in your list are: ")
    print(" ")
    for index, item in enumerate(todo_list, start=1):
                print(index,",", item)


def mark_done_func(todo_list):
    while True:    
            for index, item in enumerate(todo_list, start=1):
                print(index,",", item)
            user_input = input("choose which task you want to mark as done: ")

            if  not user_input.isdigit():
                print("Please Enter a Valid Number")
                continue

            mark_done = int(user_input)
            
            if mark_done > len(todo_list) or mark_done <=0:
                print("Please Enter a Valid Number")
                continue
                
            
            print(f"You have removed {todo_list[mark_done-1]} from you tasks. ")
            todo_list.pop(mark_done-1)
            break

       

     
        

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