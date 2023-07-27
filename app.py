from flask import Flask, render_template, request

# from flaskext.mysql import MySQL
from datetime import datetime
import json
from json import JSONEncoder
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="root", database="python_todo"
)

print(mydb)

app = Flask(__name__)

app.app_context().push()


@app.route("/", methods=["GET"])
def index():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT id,title  FROM todo_lists")
    todo_lists = mycursor.fetchall()
    print(todo_lists)

    return render_template("index.html", todo_lists=todo_lists)


@app.route("/store", methods=["POST"])
def store():
    # print(request)
    print(request.data)
    load_data = json.loads(request.data)
    print("load_data", load_data)
    title = load_data["title"]
    mycursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO todo_lists (title) VALUES (%s)"
    val = title

    mycursor.execute(sql, val)

    mydb.commit()

    return {"status": "true", "message": "Added succsfully", "data": title}


@app.route("/show")
def show():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT id,title, description FROM todo_lists")
    todo_lists = mycursor.fetchall()

    print(todo_lists)
    return "this is list of page"
    # return render_template("index.html", todo_lists=todo_lists)


@app.route("/todo/<id>", methods=["DELETE"])
def todoDelete(id):
    print("Delete ID " + id)
    mycursor = mydb.cursor()
    sql = "DELETE FROM todo_lists WHERE id = " + str(id) + " LIMIT 1"
    mycursor.execute(sql)
    mydb.commit()
    return {"status": "true", "message": "DELETED"}


@app.route("/test")
def test():
    users = user_list()
    return render_template("table.html", users=users)


def user_list():
    user1 = {
        "id": 1,
        "first_name": "Jeanette",
        "last_name": "Penddreth",
        "email": "jpenddreth0@census.gov",
        "gender": "Female",
        "ip_address": "26.58.193.2",
    }
    user2 = {
        "id": 2,
        "first_name": "Giavani",
        "last_name": "Frediani",
        "email": "gfrediani1@senate.gov",
        "gender": "Male",
        "ip_address": "229.179.4.212",
    }
    user3 = {
        "id": 3,
        "first_name": "Noell",
        "last_name": "Bea",
        "email": "nbea2@imageshack.us",
        "gender": "Female",
        "ip_address": "180.66.162.255",
    }
    user4 = {
        "id": 4,
        "first_name": "Willard",
        "last_name": "Valek",
        "email": "wvalek3@vk.com",
        "gender": "Male",
        "ip_address": "67.76.188.26",
    }
    return [user1, user2, user3, user4]


if __name__ == "__main__":
    app.run(port=5002, debug=True)
