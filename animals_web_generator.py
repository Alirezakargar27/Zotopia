import json


def serialize_animal(animal_obj):
    """
    Serializes an individual animal into an HTML list item.

    :param animal_obj: Dictionary containing animal details
    :return: HTML string representing the animal
    """
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'      <strong>Diet:</strong> {animal_obj["characteristics"].get("diet", "Unknown")}<br/>\n'
    output += f'      <strong>Location:</strong> {", ".join(animal_obj["locations"])}<br/>\n'
    output += f'      <strong>Type:</strong> {animal_obj["characteristics"].get("type", "Unknown")}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output


def generate_animal_html():
    """
    Reads the JSON file, generates HTML for all animals, and writes it to an HTML file.
    """
    # Step 1: Read the HTML template
    with open('animals_template.html', 'r') as f:
        html_template = f.read()

    # Step 2: Read the animal data from the JSON file
    with open('animals_data.json', 'r') as f:
        animals_data = json.load(f)

    # Step 3: Serialize all animal data into HTML
    animals_info = ''
    for animal in animals_data:
        animals_info += serialize_animal(animal)

    # Step 4: Replace the placeholder in the template with the animal info
    html_output = html_template.replace('__REPLACE_ANIMALS_INFO__', animals_info)

    # Step 5: Write the output to animals.html
    with open('animals.html', 'w') as f:
        f.write(html_output)

    print("HTML page generated: animals.html")


# Run the main function
if __name__ == "__main__":
    generate_animal_html()