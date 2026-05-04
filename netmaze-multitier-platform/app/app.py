from flask import Flask
import pymysql

app = Flask(__name__)

# DB config (use your RDS details)
host = "database-1-netmaze.cfwqemaqskyh.ap-south-1.rds.amazonaws.com"
user = "admin"
password = "netmazeadmin"
database = "netmaze"

@app.route('/')
def home():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            connect_timeout=5
        )

        with connection.cursor() as cursor:
            cursor.execute("SELECT file_name FROM files")
            rows = cursor.fetchall()

        connection.close()

        html = "<h1 style='color:blue;'>Netmaze File List 🚀</h1><ul>"
        for row in rows:
            html += f"<li>{row[0]}</li>"
        html += "</ul>"

        return html

    except Exception as e:
        return f"<h2 style='color:red;'>DB Error: {str(e)}</h2>"

# VERY IMPORTANT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)