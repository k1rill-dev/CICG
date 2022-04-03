from flask import Flask, render_template, redirect, url_for, request, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "dhkfblajdkvhbj"

def sql_connection():
    try:
        con = psycopg2.connect(
        database="d2hrrbu1311r1b",
        user="gahdttwnarszcm",
        password="f45246e187465ddb5c8e20b62092434faf8d59cbd6404e71d36a536a983a8af1",
        host="ec2-18-214-134-226.compute-1.amazonaws.com",
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