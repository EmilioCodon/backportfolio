# Importa las bibliotecas necesarias
from flask import Flask, request, jsonify
from flask_cors import CORS , cross_origin

app = Flask(__name__)


# Configura CORS para permitir credenciales
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'https://ubiquitous-crostata-c9a03d.netlify.app'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response



# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "https://ubiquitous-crostata-c9a03d.netlify.app"}})

# Crea una lista en memoria para almacenar datos de usuario (para demostración)
users = [
    {
        "id": 0,
        'name': 'Bull Gites',
        'email': 'bully@google.com',
        'password': 'Mincrosoft'
    },
    {
        "id": 1,
        'name': 'Mark Zumkerberg',
        'email': 'marky@facebook.com',
        'password': 'FaisBook'
    },
    {
        "id": 2,
        'name': 'Elon Tusk',
        'email': 'elont@tesla.com',
        'password': 'Telsa'
    },
    {
        "id": 3,
        'name': 'Sheryl Sandpile',
        'email': 'sheryl@linkedin.com',
        'password': 'T3D'
    }
]

next_user_id = 4

@app.route('/users', methods=['POST'])
def createUser():
    global next_user_id  # Utiliza una variable global para generar IDs únicos
    data = {
        'name': request.json.get('name'),
        'email': request.json.get('email'),
        'password': request.json.get('password'),
        'id': next_user_id  # Usa el próximo ID disponible
    }
    next_user_id += 1  # Incrementa el contador de ID para la siguiente solicitud
    users.append(data)

    return jsonify({'message': 'User created', 'user': data}), 201

# Definir una ruta para obtener todos los usuarios
@app.route('/users', methods=['GET'])
def getUsers():
    return jsonify(users)

@app.route('/user/<int:user_id>', methods=['GET'])
def getUser(user_id):
    if user_id >= 0 and user_id < len(users):
        user = users[user_id]
        user['_id'] = user_id  # Agregar el _id al usuario en la respuesta
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404


# Definir una ruta para eliminar un usuario por su ID
@app.route('/user/<int:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    if user_id >= 0 and user_id < len(users):
        deleted_user = users.pop(user_id)
        return jsonify({'message': 'User deleted', 'user': deleted_user})
    else:
        return jsonify({'message': 'User not found'}), 404

# Definir una ruta para actualizar un usuario por su ID
@app.route('/user/<int:user_id>', methods=['PUT'])
def updateUser(user_id):
    if user_id >= 0 and user_id < len(users):
        user = users[user_id]
        data = request.json
        user.update(data)
        return jsonify({'message': 'User updated', 'user': user})
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(port=4000)
