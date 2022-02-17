from flask_app import app
from flask import render_template, request, redirect

# import the class from user.py
from flask_app.models.user import User


@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.all_users()
    return render_template("index.html", all_users = users)

# ====================================
# Show One User Route
# ====================================

@app.route("/<int:user_id>")
def show_user(user_id):
    data = {
        "id" : user_id
    }
    user = User.one_user(data)
    return render_template("show_one.html", one_user = user)

# ====================================
# Add User Routes
# ====================================

@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["em"]
    }
    user_id = User.save_user(data)
    return redirect(f"/{user_id}")