
const taskForm = document.getElementById("taskForm");
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");
const taskFilter = document.getElementById("taskFilter");
const message = document.getElementById("message");

let tasks = [];

async function apiRequest(url, options = {}) {
    const response = await fetch(url, options);

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.error || "Something went wrong.");
    }

    return data;
}

async function loadTasks() {
    try {
        tasks = await apiRequest("/api/tasks");
        renderTasks();
    } catch (error) {
        message.textContent = error.message;
    }
}

function renderTasks() {
    const total = tasks.length;
    const completed = tasks.filter(task => Boolean(task.completed)).length;
    const pending = total - completed;

    document.getElementById("totalTasks").textContent = total;
    document.getElementById("completedTasks").textContent = completed;
    document.getElementById("pendingTasks").textContent = pending;

    const percentage = total
        ? Math.round((completed / total) * 100)
        : 0;

    document.getElementById("progressText").textContent =
        `${percentage}%`;

    document.getElementById("progressBar").style.width =
        `${percentage}%`;

    const filter = taskFilter.value;

    const filteredTasks = tasks.filter(task => {
        if (filter === "completed") return Boolean(task.completed);
        if (filter === "pending") return !task.completed;
        return true;
    });

    taskList.replaceChildren();

    if (!filteredTasks.length) {
        const empty = document.createElement("p");
        empty.className = "empty-state";
        empty.textContent = total
            ? "No tasks match this filter."
            : "No tasks yet. Add your first task!";

        taskList.appendChild(empty);
        return;
    }

    filteredTasks.forEach(task => {
        const item = document.createElement("div");
        item.className = "task-item";

        const left = document.createElement("div");
        left.className = "task-left";

        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.checked = Boolean(task.completed);
        checkbox.setAttribute(
            "aria-label",
            `Mark ${task.title} as completed`
        );

        checkbox.addEventListener("change", () => {
            changeTaskStatus(task.id, checkbox.checked);
        });

        const title = document.createElement("span");
        title.className = "task-title";
        title.textContent = task.title;

        if (task.completed) {
            title.classList.add("completed");
        }

        left.append(checkbox, title);

        const deleteButton = document.createElement("button");
        deleteButton.className = "delete-button";
        deleteButton.textContent = "Delete";

        deleteButton.addEventListener("click", () => {
            removeTask(task.id);
        });

        item.append(left, deleteButton);
        taskList.appendChild(item);
    });
}

taskForm.addEventListener("submit", async event => {
    event.preventDefault();

    const title = taskInput.value.trim();

    if (!title) {
        message.textContent = "Please enter a task.";
        return;
    }

    try {
        await apiRequest("/api/tasks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ title })
        });

        taskInput.value = "";
        message.textContent = "Task added successfully.";

        await loadTasks();
    } catch (error) {
        message.textContent = error.message;
    }
});

async function changeTaskStatus(id, completed) {
    try {
        await apiRequest(`/api/tasks/${id}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ completed })
        });

        message.textContent = "Task updated successfully.";
        await loadTasks();
    } catch (error) {
        message.textContent = error.message;
    }
}

async function removeTask(id) {
    if (!confirm("Are you sure you want to delete this task?")) {
        return;
    }

    try {
        await apiRequest(`/api/tasks/${id}`, {
            method: "DELETE"
        });

        message.textContent = "Task removed successfully.";
        await loadTasks();
    } catch (error) {
        message.textContent = error.message;
    }
}

taskFilter.addEventListener("change", renderTasks);

loadTasks();
