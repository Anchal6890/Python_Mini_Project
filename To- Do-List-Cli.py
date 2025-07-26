#Simple CLI To-Do List Application

todo_list = []

def show_menu():
    print("\n=== TO-DO-LIST MENU ===")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Mark Tasks as Done")
    print("4. Delete Tasks")
    print("5. Exist")

def view_tasks():
    if not todo_list:
        print("Your To-do list is empty!")
        return

    print("\nYour Tasks:")
    for idx, task in enumerate(todo_list, start=1):
       status = "✅" if task["done"] else "❌"
    print(f"{idx}. {status}{task['task']}")

def add_task():
    task = input("Enter the Task:").strip()
    if task:
        todo_list.append({"task": task, "done": False})
        print("Task Added!")
    else:
        print("Task cannot be empty.")

def mark_done():
    view_task()
    try:
        task_num = int(input("Enter task number to mark as done:"))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num -1)
            print(f"Deleted task:  {removed_task['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5):")

        if choice == '1':
            view_task()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()

   


            
            

        
        
        
        
          


    
                   

