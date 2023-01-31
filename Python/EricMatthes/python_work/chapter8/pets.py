def describe_pet(pet_name, animal_type = 'dog'):
    print("\nMy pet is " + animal_type + ".")
    print("\nMy " + animal_type + " named " + pet_name.title() + "!!!")
describe_pet(animal_type = 'dog', pet_name = 'maks')
describe_pet('muha')