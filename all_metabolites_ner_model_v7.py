# Import the required programs to execute the commands of the spaCy model

import spacy
from spacy.training.example import Example
import ast

# Load previously trained "ner_model_v6" that has been trained with preliminary data

nlp = spacy.load("ner_model_v6")  # Load your existing model

# Load the ner component

ner = nlp.get_pipe("ner")

# Read the data from the text file that converted the .csv information into a more compatible spaCy format
# This file contains approx. 3,000 metabolites that will be used to train the model.

with open("condensed_metabolite_output.txt", 'r', encoding='utf-8') as file:
    new_training_data = ast.literal_eval(file.read())

# Convert the data to spaCy examples. Each training example makes a spaCy Doc object
# It then makes a spaCy Example object from this Doc and the Example object is added to the new_examples list

new_examples = []
for data in new_training_data:
    doc = nlp.make_doc(data["text"])
    example = Example.from_dict(doc, data)
    new_examples.append(example)

# Begin training the model

nlp.begin_training()

# Set the number of training iterations, this is the number of times it will run through the training data (e.g., 50)

n_iter = 50

# Update the model and drop the losses and print them to ensure that the model is not being overfitted

for itn in range(n_iter):
    losses = {}
    for example in new_examples:
        try:
            nlp.update([example], drop=0.5, losses=losses)
        except Exception as e:
            pass  # Skip examples with errors (likely misaligned entities)
    print(losses)

# Save the updated model

nlp.to_disk("all_metabolites_ner_model_v7")
