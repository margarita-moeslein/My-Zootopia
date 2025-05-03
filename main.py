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
        # Create list item for each animal
        output += '<li class="cards__item">\n'

        # Add title with animal name
        if 'name' in animal_data:
            output += f'<div class="card__title">{animal_data["name"]}</div>\n'

        # Start paragraph for animal details
        output += '  <p class="card__text">\n'

        # Add diet if it exists
        if 'characteristics' in animal_data and 'diet' in animal_data['characteristics']:
            output += f'<strong>Diet:</strong> {animal_data["characteristics"]["diet"]}<br/>\n'

        # Add location if it exists
        if 'locations' in animal_data and len(animal_data['locations']) > 0:
            output += f'<strong>Location:</strong> {animal_data["locations"][0]}<br/>\n'

        # Add type if it exists
        if 'characteristics' in animal_data and 'type' in animal_data['characteristics']:
            output += f'      <strong>Type:</strong> {animal_data["characteristics"]["type"]}<br/>\n'

        # Close paragraph
        output += '</p>\n'

        # Close list item
        output += '</li>\n'


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