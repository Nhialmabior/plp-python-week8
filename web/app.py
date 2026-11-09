from flask import Flask, jsonify, request, render_template

from web.database import (
    initialize_database,
    get_all_tasks,
    add_task,
    update_task,
    delete_task
)

app = Flask(__name__)

initialize_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/tasks", methods=["GET"])
def list_tasks():
    return jsonify(get_all_tasks())


@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title", "")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Task title cannot be empty."}), 400

    if len(title.strip()) > 200:
        return jsonify({"error": "Task title cannot exceed 200 characters."}), 400

    task_id = add_task(title.strip())

    return jsonify({
        "message": "Task added successfully.",
        "id": task_id
    }), 201


@app.route("/api/tasks/<int:task_id>", methods=["PATCH"])
def complete_task(task_id):
    data = request.get_json(silent=True) or {}
    completed = data.get("completed")

    if not isinstance(completed, bool):
        return jsonify({"error": "A valid completion status is required."}), 400

    if not update_task(task_id, completed):
        return jsonify({"error": "Task not found."}), 404

    return jsonify({"message": "Task updated successfully."})


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    if not delete_task(task_id):
        return jsonify({"error": "Task not found."}), 404

    return jsonify({"message": "Task deleted successfully."})


if __name__ == "__main__":
    app.run(debug=True)