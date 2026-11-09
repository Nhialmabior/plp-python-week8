# Personal Mini-Toolkit – To-Do List Manager

A Python learning project developed as part of the **Power Learn Project (PLP) Python Programming – Week 8** assignment.

The project started as a command-line To-Do List Manager and was later extended into a Flask-based web application. It demonstrates fundamental Python programming concepts, web development, database integration, API development, and software testing.

## Project Overview

The Personal Mini-Toolkit is a task management application that allows users to create, view, complete, and delete tasks.

The project has two implementations:

1. **Command-Line Application:** A menu-driven Python program that manages tasks through terminal input and output.
2. **Web Application:** A Flask-powered interface with an interactive dashboard, JavaScript functionality, and SQLite database integration.

The main objective was to strengthen practical Python programming skills by building a functional application and gradually extending its capabilities.

## Features

### 1. Command-Line Application

- Add new tasks.
- View all available tasks.
- Mark tasks as completed.
- Remove tasks.
- Handle empty task entries.
- Validate task numbers.
- Handle invalid menu selections.
- Prevent tasks from being completed more than once.

### 2. Flask Web Application

- Interactive task management dashboard.
- Add and delete tasks.
- Mark tasks as completed.
- Filter tasks by status.
- Display total, pending, and completed tasks.
- Display task completion progress.
- Responsive user interface.
- REST-style API endpoints.
- SQLite database integration.
- Input validation and error handling.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| SQLite | Local database management |
| HTML5 | Web page structure |
| CSS3 | Styling and responsive design |
| JavaScript | Interactive functionality and API communication |
| unittest | Automated testing |
| Git & GitHub | Version control and project management |
| GitHub Actions | Automated test execution |

## Project Structure

```text
plp-python-week8/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── screenshots/
│   ├── menu_invalid_choice.png
│   ├── task_adding.png
│   ├── task_completed.png
│   └── task_removed.png
│
├── tests/
│   ├── test_toolkit.py
│   └── test_web.py
│
├── web/
│   ├── __init__.py
│   ├── app.py
│   ├── database.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── app.js
│
├── instance/
│   └── tasks.db
│
├── toolkit.py
├── toolkit_plan.txt
├── requirements.txt
├── README.md
└── .gitignore
```

**Note:** The `instance/tasks.db` database is generated locally when the web application runs. It is excluded from version control.

## Getting Started

### Prerequisites

- Python 3.10 or later.
- pip (Python package installer).
- Git (optional, for cloning the repository).

### 1. Clone the repository

```bash
git clone https://github.com/Nhialmabior/plp-python-week8.git
```

### 2. Navigate to the project directory

```bash
cd plp-python-week8
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Applications

### Command-Line Version

Run:

```bash
python toolkit.py
```

Follow the interactive menu to manage your tasks.

### Web Application

Run:

```bash
python -m web.app
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

You can now manage your tasks through the web interface.

## API Endpoints

The Flask application provides the following endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Load the application dashboard |
| GET | `/api/tasks` | Retrieve all tasks |
| POST | `/api/tasks` | Create a new task |
| PATCH | `/api/tasks/<id>` | Update task completion status |
| DELETE | `/api/tasks/<id>` | Delete a task |

## Automated Testing

The project includes automated tests for both the command-line and web applications.

Run the complete test suite:

```bash
python -m unittest discover -s tests -v
```

### Test Results

**14 automated tests passed successfully.**

- 8 tests for the original command-line application.
- 6 tests for the Flask web application.

The tests cover task creation, completion, deletion, input validation, and homepage functionality.

## Key Learning Outcomes

Through this project, I gained practical experience in:

- Python variables, functions, lists, loops, and conditional statements.
- Input validation and exception handling.
- Organising Python applications into modules.
- Building web applications using Flask.
- Creating and interacting with REST-style API endpoints.
- Integrating SQLite databases into Python applications.
- Connecting frontend JavaScript to backend APIs.
- Writing automated unit and application tests.
- Managing source code using Git and GitHub.
- Using GitHub Actions for continuous testing.

## Project Purpose

This is an educational and experimental project developed to strengthen practical programming skills through hands-on implementation.

It is intended for learning, practice, and demonstration of foundational software development concepts rather than production or commercial use.

## Author

**Nhial Mabior Garang**

Python Programming | Software Development | Data Analytics

- GitHub: https://github.com/Nhialmabior
- LinkedIn: https://www.linkedin.com/in/nhial-mabior/

---

*Developed as part of the Power Learn Project Africa Python Programming – Week 8 learning activities.*
