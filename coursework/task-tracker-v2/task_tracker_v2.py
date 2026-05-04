class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        self.tasks.append({"title": title, "description": description, "completed": False})
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet!")  # handles empty list case
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i}. {task['title']} - {task['description']} [{status}]")    

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

    def mark_completed(self):
        if not self.tasks:
            print("No tasks to mark!")
        else:
            task_no = int(input("Enter task number to mark as completed: "))
            if 1 <= task_no <= len(self.tasks):
                self.tasks[task_no - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid number!") 
            
manager = TaskManager()

while True:
    print("\n===== Task Tracker =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        break
    elif choice == "1":
        manager.add_task()
    elif choice == "2":
        manager.view_tasks()    
    elif choice == "3":
        manager.delete_task()
    elif choice == "4":
        manager.mark_completed()    
    else:
        print("Invalid choice! Please enter 1-5")
