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
    


@app.route('/register', methods=['POST'])
def register_user():
    users=[]
    data = request.json

    if 'name' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    name = data['name']
    email = data['email']
    password = data['password']

    # Save the user data (you may want to store it in a database in a real application)
    user = {'name': name, 'email': email, 'password': password}
    users.append(user)

    return jsonify({'message': 'User registered successfully'})


if __name__ == "__main__":
    app.run(debug=True)
