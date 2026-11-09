"""Personal Mini-Toolkit: a simple command-line to-do list manager."""


def add_task(tasks):
    """Prompt for a task and add it when the input is not empty."""
    print("\n--- Add Task ---")
    task = input("Enter a new task: ").strip()

    if task:
        tasks.append(task)
        print(f"Task added successfully: {task}")
    else:
        print("You cannot add an empty task.")


def view_tasks(tasks):
    """Display every task, or an empty-list message."""
    print("\n--- My Tasks ---")

    if not tasks:
        print("Your to-do list is empty.")
        return

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def complete_task(tasks):
    """Mark a selected task as completed."""
    print("\n--- Complete Task ---")

    if not tasks:
        print("There are no tasks to complete.")
        return

    view_tasks(tasks)
    choice = input("Enter the task number to complete: ").strip()

    if not choice.isdigit():
        print("Please enter a valid task number.")
        return

    task_number = int(choice)
    if not 1 <= task_number <= len(tasks):
        print("That task number is not on your list.")
        return

    index = task_number - 1
    if tasks[index].endswith(" [Completed]"):
        print("That task is already completed.")
    else:
        tasks[index] = f"{tasks[index]} [Completed]"
        print(f"Task completed: {tasks[index][:-12]}")


def remove_task(tasks):
    """Remove a selected task from the list."""
    print("\n--- Remove Task ---")

    if not tasks:
        print("There are no tasks to remove.")
        return

    view_tasks(tasks)
    choice = input("Enter the task number to remove: ").strip()

    if not choice.isdigit():
        print("Please enter a valid task number.")
        return

    task_number = int(choice)
    if not 1 <= task_number <= len(tasks):
        print("That task number is not on your list.")
        return

    removed_task = tasks.pop(task_number - 1)
    print(f"Task removed: {removed_task}")


def display_menu():
    """Print the application menu."""
    print("\n========== MENU ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Quit")


def main():
    """Run the to-do list application."""
    tasks = []

    print("========================================")
    print("       WELCOME TO MY TO-DO LIST")
    print("========================================")
    print("Keep track of your tasks easily!")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("\nThank you for using My To-Do List!")
            print("Goodbye! Have a productive day.")
            break
        else:
            print(f"Sorry, '{choice}' is not a valid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
