from flask import Flask, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = "secret"
db = SQLAlchemy(app)

#db model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, name, ingredients, description):
        self.name = name
        self.ingredients = ingredients
        self.description = description

#create database
db.create_all()

#variables to alter between local and production environments
local_home = '/'
prod_home = '/hello_flask.html'

@app.route(local_home, methods = ['POST', 'GET'])
def index():
    #return render_template('index.html')
    #User hit 'Add' to add a new recipe
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients']
        description = request.form['description']

        toAdd = Recipe(name, ingredients, description)
        db.session.add(toAdd)
        db.session.commit()
        return render_template("single_recipe.html", recipe = toAdd)

    #user did not hit submit, just render the home page 
    return render_template('index.html')



@app.route('/show_recipes.html')
def showRecipes():
    return render_template("show_recipes.html", recipes = Recipe.query.all())
    
    

        




if (__name__ == "__main__"):
    app.run(debug=True)
