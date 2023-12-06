from flask import Flask,jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "hello world"


# Define an API endpoint
@app.route("/api/data", methods=["GET"])
def get_data():
    data = {"key": "value", "number": 42}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
