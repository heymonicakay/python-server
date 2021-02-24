import sqlite3
import json
from models import Animal, Location

def get_all_animals():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address,
            c. name customer_name
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = a.customer_id
        """)

        animals = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                    row['location_id'], row['customer_id'])

            location = Location(row['location_id'],row['location_name'], row['location_address'])

            animal.location = location.__dict__
            animals.append(animal.__dict__)

    return json.dumps(animals)

def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        animal = Animal(data['id'], data['name'], data['breed'], data['status'],
                        data['location_id'], data['customer_id'])

        return json.dumps(animal.__dict__)

def get_animals_by_location(value):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.location_id = ?
        """, ( value, ))

        animals = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                                row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

        return json.dumps(animals)

def get_animals_by_status(value):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.status = ?
        """, ( value, ))

        animals = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                                row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

        return json.dumps(animals)

def create_animal(new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
            ( name, breed, status, location_id, customer_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_animal['name'], new_animal['breed'], new_animal['status'], new_animal['location_id'], new_animal['customer_id'], ))

        id = db_cursor.lastrowid

        new_animal['id'] = id


    return json.dumps(new_animal)

def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True

def update_animal(id, new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'], new_animal['status'], new_animal['location_id'], new_animal['customer_id'], id ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True