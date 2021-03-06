import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    query_string = str(query)
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query_string}}))
    return render_template("search.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get('username').lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"]) 
def add_recipe():
    if request.method == "POST":
        meat = "on" if request.form.get("meat") else "off"
        vegan = "on" if request.form.get("vegan") else "off"
        vegetarian = "on" if request.form.get("vegetarian") else "off"
        allergens = "on" if request.form.get("allergens") else "off"
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "cuisine_name": request.form.get("cuisine_name"),
            "description": request.form.get("description"),
            "meat": meat,
            "vegan": vegan,
            "vegetarian": vegetarian,
            "allergens": allergens,
            "created_by": session["user"],
            "directions": request.form.get("directions"),
            "ingredients": request.form.get("ingredients"),
            "prep_time": request.form.get("prep_time"),
            "total_time": request.form.get("total_time"),
            "yields": request.form.get("yields")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Succesfully Added")
        return redirect(url_for("get_recipes"))
    prep_times = mongo.db.prep_time.find().sort('prep_time', 1)
    yields = mongo.db.yields.find()
    total_times = mongo.db.total_time.find({})
    cuisines = mongo.db.cuisine.find().sort('cuisne_name', 1)
    return render_template("add_recipes.html", cuisines=cuisines, prep_times=prep_times, total_times=total_times, yeilds=yields)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        meat = "on" if request.form.get("meat") else "off"
        vegan = "on" if request.form.get("vegan") else "off"
        vegetarian = "on" if request.form.get("vegetarian") else "off"
        allergens = "on" if request.form.get("allergens") else "off"
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "cuisine_name": request.form.get("cuisine_name"),
            "description": request.form.get("description"),
            "meat": meat,
            "vegan": vegan,
            "vegetarian": vegetarian,
            "allergens": allergens,
            "created_by": session["user"],
            "directions": request.form.get("directions"),
            "ingredients": request.form.get("ingredients"),
            "prep_time": request.form.get("prep_time"),
            "total_time": request.form.get("total_time"),
            "yields": request.form.get("yields")
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, recipe)
        flash("Recipe Succesfully Updated")

    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    prep_times = mongo.db.prep_time.find().sort('prep_time', 1)
    yields = mongo.db.yields.find()
    total_times = mongo.db.total_time.find({})
    cuisines = mongo.db.cuisine.find().sort('cuisne_name', 1)
    return render_template("edit_recipe.html", recipes=recipes, cuisines=cuisines, prep_times=prep_times, total_times=total_times, yeilds=yields)


@app.route("/delete_task/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted!")
    return redirect(url_for("get_recipes"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
