# Personal Mini-Toolkit: To-Do List Manager

A beginner-friendly command-line task manager built with Python as the **PLP Week 8 Personal Mini-Toolkit project**. It provides a simple menu for creating, viewing, completing, and removing tasks.

## Features

- Add tasks to your personal list.
- View tasks with numbered positions.
- Mark tasks as completed.
- Remove tasks by their list number.
- Reject empty tasks and handle invalid menu choices or task numbers.
- Keep the menu running until the user chooses to quit.

> **Note:** Tasks are stored in memory while the program is running. They are cleared when you close the application. Persistent storage is a possible future improvement.

## Requirements

- Python 3.8 or newer
- No third-party packages required

## Getting started

1. Install Python 3 from [python.org](https://www.python.org/downloads/) if it is not already installed.
2. Clone this repository:

   ```bash
   git clone https://github.com/Nhialmabior/plp-python-week8.git
   ```

3. Open the project folder:

   ```bash
   cd plp-python-week8
   ```

4. Start the application:

   ```bash
   python toolkit.py
   ```

   On some Windows installations, use `py toolkit.py` instead.

## How to use

When the program starts, choose an option from the menu:

| Option | Action |
| --- | --- |
| 1 | Add a task |
| 2 | View all tasks |
| 3 | Mark a task as completed |
| 4 | Remove a task |
| 5 | Quit the application |

Follow the prompts and enter the task number when asked to complete or remove a task.

## Example

```text
========== MENU ==========
1. Add Task
2. View Tasks
3. Complete Task
4. Remove Task
5. Quit
Enter your choice: 1

--- Add Task ---
Enter a new task: Complete my Python assignment
Task added successfully: Complete my Python assignment
```

## Run the tests

The project includes automated unit tests using Python's built-in `unittest` framework. From the project folder, run:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions also runs these tests whenever code is pushed to `main` or a pull request targets `main`.

## Project structure

```text
plp-python-week8/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── screenshots/
│   ├── menu_invalid_choice.png
│   ├── task_adding.png
│   ├── task_completed.png
│   └── task_removed.png
├── tests/
│   └── test_toolkit.py
├── .gitignore
├── README.md
├── toolkit.py
└── toolkit_plan.txt
```

## Python concepts demonstrated

- Variables and lists
- Functions and function arguments
- `input()` and `print()`
- Conditional statements: `if`, `elif`, and `else`
- `while` and `for` loops
- f-strings
- List methods: `append()` and `pop()`
- `enumerate()` and list indexing
- String methods: `strip()`, `isdigit()`, and `endswith()`
- Input validation and the `if __name__ == "__main__"` pattern
- Basic automated testing with `unittest`

## Learning reflection

The main challenge was keeping the menu active after each operation while ensuring that the application only exits when the user selects the Quit option. Handling invalid task numbers was another important lesson: the program must validate a number before using it to access a list. Building this project strengthened my understanding of lists, loops, conditions, functions, and input validation.

## Future improvements

- Save tasks to a file so they remain available after the application closes.
- Add task priorities and due dates.
- Allow users to edit existing tasks.

## Author

**Nhial Mabior Garang**

- GitHub: [@Nhialmabior](https://github.com/Nhialmabior)

---

Created as a PLP Week 8 Python learning project.
