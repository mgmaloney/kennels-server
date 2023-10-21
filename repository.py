DATABASE = {
    "ANIMALS": [
        {
            "id": 1,
            "name": "Snickers",
            "species": "Dog",
            "locationId": 1,
            "customerId": 1,
            'status': 'admitted'
        },
        {
            "id": 2,
            "name": "Roman",
            "species": "Dog",
            "locationId": 1,
            "customerId": 2,
            'status': 'admitted'
        },
        {
            "id": 3,
            "name": "Blue",
            "species": "Cat",
            "locationId": 2,
            "customerId": 1,
            'status': 'admitted'
        }
    ],
    "EMPLOYEES": [
        {
            "id": 1,
            "name": "Jenna Solis"
        }
    ],
    "CUSTOMERS": [
        {
            "id": 1,
            "name": "Ryan Tanay"
        }
    ],
    "LOCATIONS": [
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
}


def all(resource):
    """For GET requests to collection"""
    return DATABASE[resource]


def retrieve(resource, id):
    """For GET requests for single item in collection"""
    requested_item = None
    
    for item in DATABASE[resource]:
        if item["id"] == id:
            requested_item = item
    
    return requested_item


def create(resource, item):
    """For POST requests to a collection"""
    max_id = DATABASE[resource][-1]["id"]
    new_id = max_id + 1
    item["id"] = new_id
    DATABASE[resource].append(item)
    return item   


def update(resource, id, updated_item):
    """For PUT requests to a single resource"""
    for index, item in enumerate(DATABASE[resource]):
        if item['id'] == id:
            DATABASE[resource][index] = updated_item
            break
            


def delete(resource, id):
    """For DELETE requests to a single resource"""
    item_index = -1
    for index, item in DATABASE[resource]:
        if item['id'] == id:
            item_index = index
    if item_index >= 0:
        DATABASE[resource].pop(item_index)
