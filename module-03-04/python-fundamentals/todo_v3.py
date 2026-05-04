import json

def load_tasks():
    try:
        with open("tasks.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []    
tasks = load_tasks()    

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark task done/undone")
    print("5. Quit")

    choice = input("Choose: ")

    if choice == "5":
        break
    elif choice == "1":
        task = input("Enter task name: ")
        if not task.strip():
            print("Task name cannot be empty.")
            continue
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:    
            for i, task in enumerate(tasks, 1):
                status = "✓" if task["done"] else " "
                print(f"{i}. [{status}] {task['task']}")    
    elif choice == "3":
        if not tasks:
            print("No tasks to delete")
        else:
            try:    
                delete = int(input("Which task to delete? Choose number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue    
            if 1 <= delete <= len(tasks):
                tasks.pop(delete - 1)
                save_tasks(tasks)
            else:
                print("Invalid number.")                  
    elif choice == "4":
        if not tasks:
            print("No tasks to show")
        else:
            try:
                task_no = int(input("Which task to mark? Choose number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]["done"] = not tasks[task_no - 1]["done"]
                save_tasks(tasks)
            else:
                print("Invalid number")    