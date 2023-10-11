#DOI:10.13140/RG.2.1.2119.7845
#https://www.researchgate.net/publication/261871741_Ideom-Metabolome-Adduct-Table

import csv

# Define the path to your CSV file
csv_file_path = "Metabolites.csv"

# Define the path for the output text file
output_file_path = "metabolites_output.txt"

# Initialize a list to store the data
data = []

# Read the CSV file
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header rows

    for row in reader:
        if row:
            metabolite_name = row[0]
            data.append({"text": metabolite_name, "entities": [[0, len(metabolite_name), "metabolite"]]})

# Write the data to the output text file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(str(data))
