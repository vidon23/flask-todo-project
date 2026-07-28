from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {
        "id": 1,
        "task": "Learn Flask",
        "completed": False
    },
    {
        "id": 2,
        "task": "Build Todo API",
        "completed": False
    }
]

@app.route("/")
def home():
    return jsonify(todos)

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    new_todo = request.get_json()

    if not new_todo:
        return jsonify({"error": "No data received"}), 400

    new_todo["id"] = len(todos) + 1
    todos.append(new_todo)

    return jsonify({
        "message": "Todo added successfully",
        "todo": new_todo
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)