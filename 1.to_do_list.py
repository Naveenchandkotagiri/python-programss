'''todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added.")

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

def view_tasks():
    print("Your to-do list:")
    for task in todo_list:
        print(f"- {task}")

while True:
    print("\n1. Add Task")
    print("\n2. Remove Task")
    print("\n3. View Tasks")
    print("\n4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice")'''

result=list(range(3,31,3))
print(result)