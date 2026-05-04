import json

class Task:
    def __init__(self, title, done=False, priority="normal"):
        self.title = title
        self.done = done
        self.priority = priority

    def __str__(self):
        status = "X" if self.done else " "
        return f"[{status}] {self.title} ({self.priority})"                        

    def __repr__(self):
        return f"Task(title='{self.title}', done={self.done}, priority='{self.priority}')"

    def __len__(self):
        return len(self.title)

    def __eq__(self, other):
        if not isinstance(other, Task):
            return NotImplemented
        return self.title == other.title
    

class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def delete(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks.pop(index - 1)
        else:
            print("Invalid number.") 

    def toggle(self, index):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            task.done = not task.done
        else:
            print("Invalid number")

    def view(self):
        if not self.tasks:
            print("No tasks yet!")
        else:    
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def save(self, todo_list):
        data = [
            {"title": task.title, "done": task.done, "priority": task.priority}
            for task in todo_list.tasks
        ]
        with open(self.filename, "w") as f:
            json.dump(data, f)

    def load(self, todo_list):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
            for d in data:    
                task = Task(d["title"], d["done"], d["priority"])
                todo_list.add(task)
        except FileNotFoundError:
            pass

todo_list = TodoList()
file_manager = FileManager("tasks.json")
file_manager.load(todo_list)

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
        title = input("Enter task name: ")
        if not title.strip():
            print("Task name cannot be empty.")
            continue
        todo_list.add(Task(title))
        file_manager.save(todo_list)
    elif choice == "2":
        todo_list.view()
    elif choice == "3":
        if not todo_list.tasks:
            print("No tasks to delete")
        else:
            try:    
                delete = int(input("Which task to delete? Choose number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue    
            todo_list.delete(delete)
            file_manager.save(todo_list)             
    elif choice == "4":
        if not todo_list.tasks:
            print("No tasks to show")
        else:
            try:
                task_no = int(input("Which task to mark? Choose number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            todo_list.toggle(task_no)
            file_manager.save(todo_list)
