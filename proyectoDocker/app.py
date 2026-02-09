# -- coding: utf-8 --
# Importación de módulos
from os import getenv
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId # Para manejar los IDs de MongoDB
from bson.errors import InvalidId # Para capturar errores de ID inválido

# Cargamos las variables de entorno del fichero .env
load_dotenv()

# Obtenemos la URL de MongoDB (fallback a localhost si no está en .env)
mongo_url = getenv('MONGO_URI') or 'mongodb://localhost:27017'
client = MongoClient(mongo_url)

# --- Conexión a la Base de Datos ---
# Es una buena práctica definir el cliente, la bd y la colección al principio
client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
db = client.school # Usamos la base de datos 'school'
students_collection = db.students # Usamos la colección 'students' de forma consistente

# --- Inicialización de la App Flask ---
app = Flask(__name__)

# Definición de los endpoints usando decoradores
@app.route('/', methods=['GET'])
def raiz():
    # Devolver listado de bases de datos como JSON (respuesta válida para Flask)
    """Endpoint raíz que comprueba la conexión y lista las bases de datos."""
    try:
        # list_database_names() es una buena forma de verificar la conexión
        dbs = client.list_database_names()
        return jsonify({"status": "OK", "databases": dbs})
    except Exception as e:
        # Si hay un error de conexión, lo notificamos
        return jsonify({"status": "ERROR", "message": str(e)}), 500

# Listamos a todos los estudiantes
@app.route('/students', methods=['GET'])
def list_students():
    """Obtiene todos los estudiantes de la base de datos."""
    all_students = []
    for student in students_collection.find({}):
        # Convertimos el ObjectId a string para que sea serializable en JSON
        student['_id'] = str(student['_id'])
        all_students.append(student)
    return jsonify(all_students)

# Buscamos a estudiante por id
@app.route('/student/<id_student>', methods=['GET'])
def find_student(id_student):
    """Busca un estudiante por su _id en la base de datos."""
    try:
        # Buscamos por el ObjectId de MongoDB
        student = students_collection.find_one({'_id': ObjectId(id_student)})
    except InvalidId:
        return jsonify({"error": "El formato del ID es inválido"}), 400
    
    if student:
        student['_id'] = str(student['_id'])
        return jsonify(student)
    else:
        return jsonify({"error": "Estudiante no encontrado"}), 404

# Eliminamos a un estudiante por id
@app.route('/rmstudent/<id_student>', methods=['DELETE'])
def delete_student(id_student):
    """Elimina un estudiante por su _id de la base de datos."""
    try:
        # Intentamos eliminar el documento y guardamos el resultado
        result = students_collection.delete_one({'_id': ObjectId(id_student)})
    except InvalidId:
        return jsonify({"error": "El formato del ID es inválido"}), 400

    # delete_one devuelve un objeto con 'deleted_count'. Si es 1, se borró.
    if result.deleted_count == 1:
        return jsonify({"message": f"Estudiante con id {id_student} eliminado"})
    else:
        return jsonify({"error": "Estudiante no encontrado"}), 404

# Ejecutar la aplicación (bloque colocado al final para registrar antes las rutas)
if __name__ == '__main__':
    # host='0.0.0.0' es crucial para que la app sea accesible desde fuera de un contenedor Docker
    app.run(host='0.0.0.0', port=5000, debug=True)