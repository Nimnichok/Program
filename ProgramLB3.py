from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Дані для аутентифікації
users = {
    "admin": "password123",
    "user": "password"
}

# Каталог товарів (у вигляді словника)
catalog = {}


# Аутентифікація
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    return None


# Маршрут для роботи з усіма товарами
@app.route('/items', methods=['GET', 'POST'])
@auth.login_required
def handle_items():
    if request.method == 'GET':
        return jsonify(catalog), 200

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'id' not in data or 'name' not in data or 'price' not in data:
            abort(400, description="Invalid input. Required fields: id, name, price.")

        item_id = str(data['id'])
        if item_id in catalog:
            abort(400, description=f"Item with id {item_id} already exists.")

        catalog[item_id] = {
            "name": data['name'],
            "price": data['price']
        }
        return jsonify({"message": "Item added successfully!"}), 201


# Маршрут для роботи з конкретним товаром
@app.route('/items/<id>', methods=['GET', 'PUT', 'DELETE'])
@auth.login_required
def handle_item(id):
    if id not in catalog:
        abort(404, description="Item not found.")

    if request.method == 'GET':
        return jsonify(catalog[id]), 200

    if request.method == 'PUT':
        data = request.get_json()
        if not data or 'name' not in data or 'price' not in data:
            abort(400, description="Invalid input. Required fields: name, price.")

        catalog[id].update({
            "name": data['name'],
            "price": data['price']
        })
        return jsonify({"message": "Item updated successfully!"}), 200

    if request.method == 'DELETE':
        del catalog[id]
        return jsonify({"message": "Item deleted successfully!"}), 200


# Головна сторінка
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Catalog API. Use /items and /items/<id> endpoints."})


if __name__ == '__main__':
    app.run(debug=True)
