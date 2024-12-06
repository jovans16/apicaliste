from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

#para la conexion a MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'fitness_app'
}

#creo la base de datos y tabla
def setup_database():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    cursor = conn.cursor()
    
    # creo mi base de datos
    cursor.execute("CREATE DATABASE IF NOT EXISTS fitness_app")
    cursor.execute("USE fitness_app")
    
    # aqui creo mi tabla de ejercicos segun sea 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS espalda_ejer (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        imagen_url VARCHAR(255)
    )
""")

    conn.commit()
    conn.close()

#defino mi ruta a la apliacion con flask (get_exercise)maneja la solicitud HTTP ruta /api/exercises/<int:id>,
@app.route('/api/exercises', methods=['GET'])
def get_exercises():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM exercises")
        exercises = cursor.fetchall()
        conn.close()
        return jsonify(exercises)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
#endpoint para ejercicios de abdominales
@app.route('/api/abdomen_exercises', methods=['GET'])
def get_abdomen_exercises():
    try:
        conn = mysql.connector.connect(**db_config) 
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM abdomen_exercises")
        abdomen_exercises = cursor.fetchall()
        conn.close()
        return jsonify(abdomen_exercises)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint para ejercicios de espalda
@app.route('/api/espalda_ejer', methods=['GET'])
def get_espalda_exercises():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        # Realizar la consulta para obtener los ejercicios de espalda
        cursor.execute("SELECT * FROM espalda_ejer") 
        
        espalda_ejer = cursor.fetchall()
        conn.close()
        return jsonify(espalda_ejer)    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Endpoint para ejercicios de pecho
@app.route('/api/pecho_ejer', methods=['GET'])
def get_pecho_exercises():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        # Realizar la consulta para obtener los ejercicios de espalda
        cursor.execute("SELECT * FROM pecho_ejer") 
        
        pecho_ejer = cursor.fetchall()
        conn.close()
        return jsonify(pecho_ejer)    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint para ejercicios de piernas
@app.route('/api/piernas_ejer', methods=['GET'])
def get_piernas_exercises():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        # Realizar la consulta para obtener los ejercicios de espalda
        cursor.execute("SELECT * FROM piernas_ejer") 
        
        piernas_ejer = cursor.fetchall()
        conn.close()
        return jsonify(piernas_ejer)    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint para dietas
@app.route('/api/dietas', methods=['GET'])
def get_dietas():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Realizar la consulta para obtener las dietas
        cursor.execute("SELECT * FROM dietas")
        
        dietas = cursor.fetchall()
        conn.close()
        return jsonify(dietas)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint para todo el cuerpo
@app.route('/api/todo_ejer', methods=['GET'])
def get_todo_exercises():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Realizar la consulta para obtener las dietas
        cursor.execute("SELECT * FROM todo_ejer")
        
        todo_ejer = cursor.fetchall()
        conn.close()
        return jsonify(todo_ejer)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500






if __name__ == '__main__':
    setup_database()
    app.run(debug=True, host='0.0.0.0', port=5000)
