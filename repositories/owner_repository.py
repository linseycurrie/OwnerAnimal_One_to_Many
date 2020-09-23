from db.run_sql import run_sql
from models.animal import Animal
from models.owner import Owner


def save(owner):
    sql = "INSERT INTO owners (name) VALUES (%s) RETURNING *"
    values = [owner.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner


def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results is not None:
        owner = Owner(results['name'], results['id'])
    return owner

def select_all():
    owners= []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['name'])
        owners.append(owner)
    return owners