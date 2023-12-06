from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "hello world"


# Define an API endpoint
@app.route("/api/data", methods=["GET"])
def get_data():
    data = {"key": "value", "number": 42}
    return jsonify(data),200


@app.route("/post", methods=["POST"])
def post_data():
    if request.is_json:
        data = request.get_json()
        print("received JSON data: ", data)
        return jsonify(data),201


if __name__ == "__main__":
    app.run(debug=True)
