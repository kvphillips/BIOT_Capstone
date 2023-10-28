#import corresponding libraries to run program

import csv

# the path to your CSV file

csv_file_path = "tomato_metabolite_v1.csv"

# setup the path for the output text file that will be fed into the NER model

output_file_path = "tomato_metabolite_v1.txt"

# setup list to store data

data = []

# read the CSV file

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header rows

# for loop to identify and make text and entity associations for the label metabolite    
    
    for row in reader:
        if row:
            metabolite_name = row[0]
            data.append({"text": metabolite_name, "entities": [[0, len(metabolite_name), "metabolite"]]})

# data is written to the output text file

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(str(data))
