import json

ANIMAL_HTML_TEMPLATE = "animals_template.html"
REPLACED_TEXT = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
  """Loads a JSON file"""
  with open(file_path, "r") as handle:
    return json.load(handle)


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


def generate_html(file_path, animals_data):
    with open(ANIMAL_HTML_TEMPLATE, 'r') as fileobj:
        template_content = fileobj.read()

    output = ''  # define an empty string
    for animal_data in animals_data:
        # For each animal, create entries with proper newlines
        animal_output = ""

        # Add name if it exists
        if 'name' in animal_data:
            animal_output += f"Name: {animal_data['name']}\n"

        # Add diet if it exists
        if 'characteristics' in animal_data and 'diet' in animal_data['characteristics']:
            animal_output += f"Diet: {animal_data['characteristics']['diet']}\n"

        # Add location if it exists
        if 'locations' in animal_data and len(animal_data['locations']) > 0:
            animal_output += f"Location: {animal_data['locations'][0]}\n"

        # Add type if it exists
        if 'characteristics' in animal_data and 'type' in animal_data['characteristics']:
            animal_output += f"Type: {animal_data['characteristics']['type']}\n"

        # Add empty line between animals
        animal_output += "\n"

        # Add this animal's info to the overall output
        output += animal_output

    # Replace the placeholder with our generated content
    html_content = template_content.replace(REPLACED_TEXT, output)

    # Write to the output file
    with open(file_path, 'w') as fileobj:
        fileobj.write(html_content)

    print(f"HTML file successfully generated: {file_path}")

    html_content = template_content.replace(REPLACED_TEXT, output)
    with open(file_path, 'w') as fileobj:
        fileobj.write(html_content)



def main():
    try:
        animals_data = load_data('animals_data.json')
        print_animal_info(animals_data)
        generate_html('animals.html', animals_data)
    except Exception as e:
        print(f"Error processing file: {e}")




if __name__ == "__main__":
    main()