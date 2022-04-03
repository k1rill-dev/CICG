from flask import Flask, render_template, redirect, url_for, request, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "dhkfblajdkvhbj"

def sql_connection():
    try:
        con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="KOKI___KLAVY123",
        host="localhost",
        port="5432"
    )
        return con
    except Exception as ex:
        print(ex)

cur = sql_connection().cursor()

@app.route('/', methods=['POST', 'GET'])
def index():
    cur.execute("SELECT * FROM PLAYERS")
    rows = cur.fetchall()
    return render_template("index.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)