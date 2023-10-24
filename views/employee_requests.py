import sqlite3
import json
from models import Employee, Location

EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    }
]


def get_all_employees():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id,
            l.name location_name,
            l.address location_address
        FROM employee a
        JOIN location l
            ON l.id = a.location_id
        """)
        
        employees = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            location = Location(row["id"], row["location_name"], row["location_address"])
            employee.location = location.__dict__
            employees.append(employee.__dict__)
            
        return employees
    
def get_single_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a                   
        WHERE id = ?
        """, (id, ))
        
        data = db_cursor.fetchone()
        
        employee = Employee(data['id'], data['name'], data['address'], data['location_id'])
        return employee.__dict__

def get_employees_by_location(location_id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.location_id
        FROM Employee c
        WHERE location_id = ?                  
        """, (location_id, ))
        
        employees = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            employee = Employee(row["id"], row["name"], row["address"], row["location_id"])
            employees.append(employee.__dict__)
        
        return employees

def delete_employee(id):
    with sqlite3.connect('./kennel.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?                  
        """, (id,))

# pre sql refactor
# def get_all_employees():
#     return EMPLOYEES

# def get_single_employee(id):
#     requested_employee = None
    
#     for employee in EMPLOYEES:
#         if employee['id'] == id:
#             requested_employee = employee
    
#     return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]['id']
    new_id = max_id + 1
    employee['id'] = new_id
    EMPLOYEES.append(employee)
    return employee

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee['id'] == id:
            EMPLOYEES[index] = new_employee
            break
