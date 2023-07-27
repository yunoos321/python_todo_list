from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "hardsecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/python_todo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# basic model
class TodoList(db.Model):
    __tablename__ = "todo_lists"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, index=True)
    description = db.Column(db.String(128))


def __init__(self, title, description):
    self.title = title
    self.description = description


@app.route("/")
def index():
    users = user_list()
    return render_template("index.html", users=users)


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


@app.route("/test")
def test():
    return {"demo": "Hello Test page"}


if __name__ == "__main__":
    app.run(port=5002, debug=True)
