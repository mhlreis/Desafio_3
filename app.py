from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_Host'] = 'localhost' #127.0.0.1
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'devweb'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/templates/contato.html", methods=['POST', 'GET'])
def contato():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute(f'INSERT INTO contatos(email, assunto, descricao) VALUES ("{email}", "{assunto}", "{descricao}")')

        mysql.connection.commit()

        cur.close()

        return 'Concluído'
    return render_template("contato.html")

@app.route("/templates/quemsomos.html")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/templates/users.html")
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contatos")

    if users > 0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails)
