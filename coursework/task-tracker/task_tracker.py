class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        self.tasks.append({"title": title, "description": description})
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet!")  # handles empty list case
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task['title']}: {task['description']}")    

    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete!")  # handles empty list case
        else:
            delete = int(input("Which task to delete? Choose number: "))
            if 1 <= delete <= len(self.tasks):
                self.tasks.pop(delete - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid number!")  # handles out of range input        

manager = TaskManager()

while True:
    print("\n===== Task Tracker =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "4":
        break
    elif choice == "1":
        manager.add_task()
    elif choice == "2":
        manager.view_tasks()    
    elif choice == "3":
        manager.delete_task()
    else:
        print("Invalid choice! Please enter 1-4")
