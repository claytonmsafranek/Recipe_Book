from flask import Flask, render_template, redirect, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#configure mysql connection
app.config['MYSQL_HOST'] = 'ec2-44-202-119-23.compute-1.amazonaws.com'
app.config['MYSQL_USER'] = 'remoteuser'
app.config['MYSQL_PASSWORD'] = '@ranD0m1!'
app.config['MYSQL_DB'] = 'testDB'
mysql = MySQL(app)


#variables to alter between local and production environments
local = '/'
prod = '/hello_flask.html'

@app.route(local)
def index():
    return render_template('index.html')

@app.route('/info', methods = ['POST', 'GET'])
def getInfo():
    if request.method == 'GET':
        return redirect('/')
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO testTable (NAME, AGE) VALUES(%s,%s)''', (name, age))
        mysql.connection.commit()
        cursor.close()
        return "Done!"




if (__name__ == "__main__"):
    app.run(debug=True)
