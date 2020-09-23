from flask import Flask, render_template, request, redirect

from models.animal import Animal

from flask import Blueprint
from repositories import animal_repository, owner_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def tasks():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", all_animals= animals)

@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete(id):
    animal_repository.delete(id)
    return redirect("/animals")

@animals_blueprint.route("/animals/new")
def new_animal():
    all_owners = owner_repository.select_all()
    return render_template("animals/new.html", all_owners=all_owners)

@animals_blueprint.route("/animals", methods=['POST'])
def create():
    name = request.form['name']
    animal_type = request.form['animal_type']
    owner_id = request.form['owner_id']
    owner = owner_repository.select(owner_id)
    new_animal = Animal(name, animal_type, owner)
    animal_repository.save(new_animal)
    return redirect("/animals")

@animals_blueprint.route("/animals/<id>", methods=['GET'])
def display_animal(id):
    animal = animal_repository.select(id)
    return render_template("/index.html", animal=animal)
