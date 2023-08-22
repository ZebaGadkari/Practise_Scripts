tasks = []

def add_task(description, due_date):
    tasks.append({"description": description, "due_date": due_date, "completed": False})

def view_tasks():
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['description']} - Due Date: {task['due_date']} - Status: {status}")

def mark_completed(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
    else:
        print("Invalid task index!")

def remove_completed():
    global tasks
    tasks = [task for task in tasks if not task["completed"]]

# Main loop
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Mark Completed\n4. Remove Completed\n5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        description = input("Enter task description: ")
        due_date = input("Enter due date (e.g., YYYY-MM-DD): ")
        add_task(description, due_date)

    elif choice == 2:
        view_tasks()

    elif choice == 3:
        task_index = int(input("Enter the task index to mark as completed: "))
        mark_completed(task_index)

    elif choice == 4:
        remove_completed()

    elif choice == 5:
        print("Exiting the To-Do List Application.")
        break

    else:
        print("Invalid choice. Please try again.")
