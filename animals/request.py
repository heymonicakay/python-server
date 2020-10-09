ANIMALS = [
    {
      "id": 1,
      "name": "Doodles",
      "breed": "Poodle",
      "customerId": 1,
      "locationId": 2,
      "status": "Admitted"
    },
    {
      "id": 2,
      "name": "Kaos",
      "breed": "Aussie-Shep",
      "customerId": 2,
      "locationId": 1,
      "status": "Admitted"
    },
    {
      "id": 3,
      "name": "Rufus",
      "breed": "Basset",
      "customerId": 3,
      "locationId": 2,
      "status": "Admitted"
    }
]

def get_all_animals():
    return ANIMALS


def get_single_animal(id):
    requested_animal = None

    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal

def create_animal(animal):
    max_id = ANIMALS[-1]["id"]

    new_id = max_id + 1

    animal["id"] = new_id

    ANIMALS.append(animal)

    return animal

def delete_animal(id):
    animal_index = -1

    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            animal_index = index

    if animal_index >= 0:
        ANIMALS.pop(animal_index)

def update_animal(id, new_animal):
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            ANIMALS[index] = new_animal
            break