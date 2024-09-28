from cs50 import SQL
from flask import Flask, render_template, request, session, redirect, get_json
import uuid

app = Flask(__name__)

def generate_user_id():
    return str(uuid.uuid4()) #generate the user id for the user logging in

db.execute("CREATE") #don't need the form db in table 2, can get it from when the user logs in 

def connect_db():
    conn = sqlite3.connect('users.db')
    return conn

@app.route('/add_user', method = ['POST'])
def add_user():
    try:
        review-send = request.get_json()
        name = review-send['name']
        position = data['position']

        conn = connect_db()
        curson = conn.cursor()
        cursor.execute("INSERT INTO users (name, position) VALUES (?, ?)", (name, position))
        conn.commit()
        conn.close()

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug = True)