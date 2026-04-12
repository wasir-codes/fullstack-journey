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
    
class PriorityTask(Task):
    def __init__(self, title, deadline, done=False, priority="high"):
        super().__init__(title, done, priority)
        self.deadline = deadline

    def __str__(self):
        return f"{super().__str__()} — due: {self.deadline}"

p = PriorityTask("Buy Milk", "15-04-2026")


p = PriorityTask("Submit assignment", "2024-12-31")
print(p)
print(repr(p))
print(len(p))

# test that Task methods still work on PriorityTask
p.done = True
print(p)