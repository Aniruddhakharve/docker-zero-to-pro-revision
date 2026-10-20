import os
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppass_local_only")
DB_NAME = os.getenv("DB_NAME", "appdb")


def check_db():
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            return cursor.fetchone()[0]
    finally:
        conn.close()


@app.get("/")
def home():
    return jsonify({"message": "flask-mysql lab", "db_check": check_db()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
