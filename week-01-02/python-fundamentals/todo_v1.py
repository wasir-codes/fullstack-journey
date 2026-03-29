tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

    choice = input("Choose: ")

    if choice == "4":
        break
    elif choice == "1":
        task = input("Enter task name: ")
        tasks.append(task)
    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:    
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == "3":
        if not tasks:
            print("No tasks to delete")
        else:    
            delete = int(input("Which task to delete? Choose number: "))
            if 1 <= delete <= len(tasks):
                tasks.pop(delete - 1)
            else:
                print("Invalid number.")                  
