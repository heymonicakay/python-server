import sqlite3
import json
from models import Employee, Location


def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id,
            e.address
        FROM employee e
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            employee = Employee(row['id'], row['name'], row['location_id'], row['address'])

            employees.append(employee.__dict__)

    return json.dumps(employees)


def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id,
            e.address,
            l.name location_name,
            l.address location_address
        FROM employee e
        JOIN location l ON l.id = e.location_id
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['location_id'], data['address'])

        location = Location("", data['location_name'], data['location_address'])
        employee.location = location.__dict__

        return json.dumps(employee.__dict__)

def create_employee(new_employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name, location_id, address)
        VALUES
            ( ?, ?, ?);
        """, (new_employee['name'], new_employee['location_id'],
new_employee['address']))


        id = db_cursor.lastrowid


        new_employee['id'] = id


    return json.dumps(new_employee)

def delete_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True

def update_employee(id, new_employee):
    with sqlite3.connect("./kennel.db") as conn:

        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Employee
            SET
                e.id,
                e.name,
                e.location_id,
                e.address
        WHERE id = ?
        """, (new_employee['name'], new_employee['location_id'], new_employee['address'], id ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def get_employee_by_location(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id,
            e.address
        FROM employee e
        WHERE e.location_id = ?
        """, ( location_id, ))

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            employee = Employee(row['id'], row['name'], row['location_id'], row['address'])

            employees.append(employee.__dict__)

        return json.dumps(employees)