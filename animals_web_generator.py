import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_info(animals):
    """ Prints information about each animal """
    for animal in animals:
        # Start with the name which should be present
        output_parts = [f"Name: {animal['name']}"]

        # Add diet if it exists
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output_parts.append(f"Diet: {animal['characteristics']['diet']}")

        # Add first location if locations exist and have at least one entry
        if 'locations' in animal and len(animal['locations']) > 0:
            output_parts.append(f"Location: {animal['locations'][0]}")

        # Add type if it exists
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output_parts.append(f"Type: {animal['characteristics']['type']}")

        # Join all parts with spaces and print
        print(" ".join(output_parts))


def main():
    try:
        animals_data = load_data('animals_data.json')
        print_animal_info(animals_data)
    except Exception as e:
        print(f"Error processing file: {e}")


if __name__ == "__main__":
    main()