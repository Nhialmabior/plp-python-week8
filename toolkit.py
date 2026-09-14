# Personal Mini-Toolkit: To-Do List Manager

# This list stores all tasks while the program is running.
tasks = []


# This tool adds a new task to the to-do list.
def add_task():
    print("\n--- Add Task ---")

    task = input("Enter a new task: ").strip()

    if task:
        tasks.append(task)
        print(f"Task added successfully: {task}")
    else:
        print("You cannot add an empty task.")


# This tool displays all tasks currently in the list.
def view_tasks():
    print("\n--- My Tasks ---")

    if not tasks:
        print("Your to-do list is empty.")
    else:
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")


# This tool marks a selected task as completed.
def complete_task():
    print("\n--- Complete Task ---")

    if not tasks:
        print("There are no tasks to complete.")
        return

    view_tasks()

    choice = input("Enter the task number to complete: ").strip()

    if choice.isdigit():
        task_number = int(choice)

        if 1 <= task_number <= len(tasks):
            completed_task = tasks[task_number - 1]

            if "[Completed]" not in completed_task:
                tasks[task_number - 1] = f"{completed_task} [Completed]"
                print(f"Task completed: {completed_task}")
            else:
                print("That task is already completed.")
        else:
            print("That task number is not on your list.")
    else:
        print("Please enter a valid task number.")


# This tool removes a selected task from the to-do list.
def remove_task():
    print("\n--- Remove Task ---")

    if not tasks:
        print("There are no tasks to remove.")
        return

    view_tasks()

    choice = input("Enter the task number to remove: ").strip()

    if choice.isdigit():
        task_number = int(choice)

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task removed: {removed_task}")
        else:
            print("That task number is not on your list.")
    else:
        print("Please enter a valid task number.")


# Main program menu.
print("========================================")
print("       WELCOME TO MY TO-DO LIST")
print("========================================")
print("Keep track of your tasks easily!")

while True:
    print("\n========== MENU ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Quit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        remove_task()

    elif choice == "5":
        print("\nThank you for using My To-Do List!")
        print("Goodbye! Have a productive day.")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please select 1-5.")