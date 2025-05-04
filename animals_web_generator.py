"""
Module for generating HTML content from data
"""


# Constants
ANIMAL_HTML_TEMPLATE = "animals_template.html"
REPLACED_TEXT = "__REPLACE_ANIMALS_INFO__"


def serialize_animal(animal_data):
    """Convert a single animal object into HTML format"""
    output = '<li class="cards__item">\n'

    # add title with animal name
    if 'name' in animal_data:
        output += f'<div class="card__title">{animal_data["name"]}</div>\n'

    # start paragraph for animal details
        output += '<p class="card__text">\n'

    # add diet if it exists
    if 'characteristics' in animal_data and 'diet' in animal_data['characteristics']:
        output += f'<strong>Diet:</strong> {animal_data["characteristics"]["diet"]}<br/>\n'

    # add location if it exists
    if 'locations' in animal_data and len(animal_data['locations']) > 0:
        output += f'<strong>Location:</strong> {animal_data["locations"][0]}<br/>\n'

    # add type if it exists
    if 'characteristics' in animal_data and 'type' in animal_data['characteristics']:
        output += f'<strong>Type:</strong> {animal_data["characteristics"]["type"]}<br/>\n'

    # close paragraph and list item
    output += '</p>\n'
    output += '</li>\n'

    return output


def generate_html(file_path, animals_data):
    with open(ANIMAL_HTML_TEMPLATE, 'r') as fileobj:
        template_content = fileobj.read()

    # Generate HTML for all animals
    output = ''
    for animal_data in animals_data:
        output += serialize_animal(animal_data)

    # Replace the placeholder with generated content
    html_content = template_content.replace(REPLACED_TEXT, output)

    # Write to the output file
    with open(file_path, 'w') as fileobj:
        fileobj.write(html_content)

    print(f"HTML file successfully generated: {file_path}")