import csv

# Define the path to your CSV file
csv_file_path = "tomato_health_v1.csv"

# Define the path for the output text file
output_file_path = "tomato_health_v1.txt"

# Initialize a list to store the data
data = []

# Read the CSV file
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header rows

    for row in reader:
        if row:
            health_benefit_name = row[0]
            data.append({"text": health_benefit_name, "entities": [[0, len(health_benefit_name), "health benefit"]]})

# Write the data to the output text file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(str(data))
