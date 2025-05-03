"""
Main entry point for the application.
"""

from data_loader import load_data
from console_printer import print_animal_info
from animals_web_generator import generate_html


def main():
    try:
        animals_data = load_data('animals_data.json')
        print_animal_info(animals_data)
        generate_html('animals.html', animals_data)
    except Exception as e:
        print(f"Error processing file: {e}")


if __name__ == "__main__":
    main()