"""
Module for displaying information in the console
"""


def print_animal_info(animals):
    """Print information about each animal"""
    for animal in animals:
        output_animal_list = []
        if 'name' in animal:
            output_animal_list.append(f"Name: {animal['name']}")

        # add diet if it exists
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output_animal_list.append(f"Diet: {animal['characteristics']['diet']}")

        # add first location if locations exist and have at least one entry
        if 'locations' in animal and len(animal['locations']) > 0:
            output_animal_list.append(f"Location: {animal['locations'][0]}")

        # add type if it exists
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output_animal_list.append(f"Type: {animal['characteristics']['type']}")

        # print each item on a new line
        print("\n".join(output_animal_list))
        print()  # add an empty line between animals