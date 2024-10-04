class ToDoList:
    def __init__(self, tasks: list[str]) -> None:
        self.tasks = tasks

    def __repr__(self) -> str:
        return f"ToDoList(tasks: {self.tasks})"

    def __str__(self) -> str:
        return "\n".join(self.tasks)

    def __add__(self, other: 'ToDoList') -> 'ToDoList':
        return ToDoList(self.tasks + other.tasks)



tasks = ['task1', 'task2']

list1 = ToDoList(tasks)

print(repr(list1))


print(list1)

list2 = ToDoList(['task3', 'task4'])

list3 = list1 + list2

print(list3)

