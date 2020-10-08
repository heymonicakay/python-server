EMPLOYEES = [
    {
      "id": 1,
      "name": "Mario Kart",
      "animalId": 2,
      "locationId": 1
    },
    {
      "id": 2,
      "name": "Mark Ruffullo",
      "animalId": 2,
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Luke Bryan",
      "locationId": 1,
      "animalId": 2
    },
    {
      "name": " Sarah Anderson",
      "locationId": 1,
      "animalId": 2,
      "id": 4
    },
    {
      "name": "Sally Fields",
      "locationId": 2,
      "animalId": 3,
      "id": 5
    },
    {
      "name": "Bill Hillsman",
      "locationId": 2,
      "animalId": 3,
      "id": 6
    }
]


def get_all_employees():
    return EMPLOYEES

    # Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee