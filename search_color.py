import csv
import sys
import pyperclip


# Load color profile data into dictionary
with open('color_profiles.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)  # skip the header row
    color_profile = {}
    for row in reader:
        rgb = tuple(map(int, row[0][1:-1].split(',')))
        hex_code = row[1]
        name = row[2]
        color_profile[name] = (rgb, hex_code)

# Define main function to search for a color by name and print its hex code to the console
def search_color(search_term):
    search_term = search_term.lower()
    if search_term == 'exit':
        return
    matching_names = []
    for name in color_profile.keys():
        if search_term in name.lower():
            matching_names.append(name)
    if not matching_names:
        print(f"No color found with name '{search_term}'.")
    elif len(matching_names) == 1:
        name = matching_names[0]
        rgb, hex_code = color_profile[name]
        print(f"Hex code for color '{name}': {hex_code}")
    else:
        print(f"Multiple colors found with name containing '{search_term}':")
        for i, name in enumerate(matching_names):
            print(f"{i+1}. {name}")
        print("Please select the color you want by entering its number:")
        selection = input()
        while not selection.isdigit() or int(selection) not in range(1, len(matching_names)+1):
            print("Invalid selection. Please enter a number between 1 and {len(matching_names)}.")
            selection = input()
        name = matching_names[int(selection)-1]
        rgb, hex_code = color_profile[name]
        pyperclip.copy(hex_code)
        print(f"Hex code for color '{name}': {hex_code} is coppied to clipboard")

if __name__ == '__main__':

    while True:
        search_term = input("Enter a color name to search for (or 'exit' to quit): ").lower()
        if search_term == 'exit':
            break
        search_color(search_term)
 