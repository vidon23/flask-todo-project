from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Todo Project Running"

@app.route("/api")
def api():
    data = {
        "message": "Hello from API"
    }
    return jsonify(data)

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    itemName = "demo item"
    itemDescription = "demo description"

    return jsonify({
        "itemName": itemName,
        "itemDescription": itemDescription,
        "message": "Todo saved"
    })
if __name__ == "__main__":
    app.run(debug=True)