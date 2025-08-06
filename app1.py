from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "✅ Flask REST API is Running!"

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({'error': 'Username and email are required'}), 400

    users[username] = {'email': email}
    print(f"[SERVER LOG] ➕ Added user: {username}")
    return jsonify({'message': f'User {username} added'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    print("[SERVER LOG] 📥 Fetched all users")
    return jsonify(users), 200

@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    if username not in users:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    email = data.get('email')
    users[username]['email'] = email
    print(f"[SERVER LOG] 🔄 Updated user: {username}")
    return jsonify({'message': f'User {username} updated'}), 200

if __name__ == '__main__':
    app.run(debug=True)
