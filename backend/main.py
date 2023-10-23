from flask import Flask, jsonify, request, Response, render_template
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/users/*": {"origins": "*"}})

users = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }, {
        "id": 2,
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }, {
        "id": 3,
        "name": "Josh Duhamel",
        "email": "josh@email.com"
    }
]


@app.route('/users', methods=["GET", "POST"])
def get_users():
    return jsonify(users)


@app.route('/users/{item_id}', methods=["GET", "POST", "PUT", "DELETE"])
def get_id(item_id):
    user = [user for user in users if user["id"] == item_id][0]
    return jsonify(user)


@app.errorhandler(404)
def not_found():
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
