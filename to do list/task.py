f = open ("tasks.txt", 'r')


def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def save_tasks(tasks):
    with open("tasks.txt", 'w') as f:
        for task in tasks:
            f.write(task + '\n')
    print("Tasks saved to tasks.txt.")


def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", 'r') as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("No saved tasks found.")
    return tasks

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        print("Task deleted!\n")
    except:
        print("Invalid choice.\n")
    

def main():
    tasks = load_tasks()

    while True:
        print("----- TO-DO LIST -----")
        print("1. Add Task")
        print("2. View Tasks") 
        print("3. Delete Task")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
          delete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()