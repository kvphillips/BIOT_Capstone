import spacy
from spacy.training.example import Example
import ast

nlp = spacy.load("ner_model_v6")  # Load your existing model
ner = nlp.get_pipe("ner")

# Read the data from the text file
with open("condensed_metabolite_output.txt", 'r', encoding='utf-8') as file:
    new_training_data = ast.literal_eval(file.read())

new_examples = []
for data in new_training_data:
    doc = nlp.make_doc(data["text"])
    example = Example.from_dict(doc, data)
    new_examples.append(example)

# Set the number of training iterations (e.g., 10)
nlp.begin_training()
n_iter = 50

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
