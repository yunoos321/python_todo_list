from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from json import JSONEncoder


app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///python_todo.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/python_todo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.app_context().push()
db = SQLAlchemy(app)
app.app_context().push()


# basic model
class TodoList(db.Model):
    # __tablename__ = "todo_lists"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    # description = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # with app.app_context():
    #     db.create_all()

    # def __reps__(self) -> str:
    # return f" {self.id} - {self.title} "


def __init__(self, title):
    self.title = title
    # self.description = description


@app.route("/", methods=["GET"])
def index():
    # if request.method == "POST":
    #     print(request.form["title"])
    # todo = TodoList(title="First todo")
    # db.session.add(todo)
    # db.session.commit()
    todo_lists = TodoList.query.all()
    return render_template("index.html", todo_lists=todo_lists)


@app.route("/store", methods=["POST"])
def store():
    # print(request)
    print(request.data)
    load_data = json.loads(request.data)
    print("load_data", load_data)
    title = load_data["title"]
    todo = TodoList(title=title)
    db.session.add(todo)
    db.session.commit()

    return {"status": "true", "message": "Added succsfully", "data": title}


@app.route("/show")
def show():
    todo_lists = TodoList.query.all()
    print(todo_lists)
    return "this is list of page"
    # return render_template("index.html", todo_lists=todo_lists)


@app.route("/todo/<id>", methods=["DELETE"])
def todoDelete(id):
    guide = TodoList.query.get(id)
    # print(guide)
    db.session.delete(guide)
    db.session.commit()

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
