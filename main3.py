from flask import Flask, request
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host='localhost',
    user='your_mysql_username',
    password='your_mysql_password',
    database='your_database_name'
)

@app.route('/validate', methods=['POST'])
def validate_user():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor = db.cursor()
    query = "SELECT * FROM login WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return 'User validation successful'
    else:
        return 'Invalid username or password'

if __name__ == '__main__':
    app.run()

