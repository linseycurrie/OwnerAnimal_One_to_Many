from db.run_sql import run_sql
from models.animal import Animal
from models.owner import Owner
import repositories.owner_repository as owner_repository

def save(animal):
    sql = "INSERT INTO animals (name, type, owner_id) VALUES (%s, %s, %s) RETURNING *"
    values = [animal.name, animal.type, animal.owner.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal


def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for row in results:
        owner = owner_repository.select(row['owner_id'])
        animal = Animal(row['name'], row['type'], owner)
        animals.append(animal)
    return animals


def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)