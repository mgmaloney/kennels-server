import sqlite3
import json
from models import Location
from .employee_requests import get_employees_by_location
from .animal_requests import get_animals_by_location

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]

def get_all_locations():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)
        
        locations = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            location = Location(row['id'], row['name'], row['address'])
            locations.append(location.__dict__)
        return locations

def get_single_location(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?        
        """, (id, ))
       
        data = db_cursor.fetchone()
        
        animals = get_animals_by_location(id)
        
        employees = get_employees_by_location(id)
        
        location = Location(data['id'], data['name'], data['address'])
        location.employees = employees
        location.animals = animals
        
        return location.__dict__
        

# pre-sql db refactor 
# def get_all_locations():
#     return LOCATIONS


# def get_single_location(id):
#     requested_location = None
    
#     for location in LOCATIONS:
#         if location['id'] == id:
#             requested_location = location
    
#     return requested_location

def create_location(location):
    max_id = LOCATIONS[-1]['id']
    new_id = max_id + 1
    location['id'] = new_id
    LOCATIONS.append(location)
    return location

def delete_location(id):
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location['id'] == id:
            location_index == index
    
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location['id'] == id:
            LOCATIONS[index] = new_location
            break
