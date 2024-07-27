import csv
import re

# Define the input and output file paths
input_file = 'C:/Users/danie/OneDrive/Software/KSP Science Checklist/persistent, short.txt'
output_file = 'C:/Users/danie/OneDrive/Software/KSP Science Checklist/output all science.csv'

# Define a regex pattern to match each science block
science_pattern = re.compile(r'Science\s*\{([^}]+)\}')

# Read the input file
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

# Find all science blocks
science_blocks = science_pattern.findall(content)

# Define the CSV header
header = ['id', 'title', 'dsc', 'scv', 'sbv', 'sci', 'asc', 'cap']

# Function to replace decimal points with commas
def replace_decimal_point(value):
    try:
        # Only replace if the value is a float or contains a decimal point
        if '.' in value:
            return value.replace('.', ',')
        return value
    except TypeError:
        return value

# Open the output CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    csvwriter.writerow(header)  # Write the header

    # Process each science block
    for block in science_blocks:
        # Extract each field
        data = {}
        for line in block.split('\n'):
            if '=' in line:
                key, value = map(str.strip, line.split('=', 1))
                data[key] = replace_decimal_point(value)  # Replace decimal points with commas

        # Write the data to the CSV file
        csvwriter.writerow([data.get(key, '') for key in header])

print("Daten wurden erfolgreich in die CSV-Datei übertragen.")
