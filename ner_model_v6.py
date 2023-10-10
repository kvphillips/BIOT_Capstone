# Import the required programs to execute the commands of the spaCy code

import spacy
from spacy.training.example import Example

# Load previously trained preliminary model
# Minimal training occurred in ner_model_v5
# A few catchphrases and labels related to health benefits and metabolites were used to construct the model correctly

nlp = spacy.load("ner_model_v5")

# Load the ner component

ner = nlp.get_pipe("ner")

# Included the list of labeled metabolites and health benefits within the list of code
# This information was from .csv file that used additional python code to format in the following way
# This data will be used to begin the first formal training of the model

new_training_data = [
    {"text": "antioxidant", "entities": [[0, 11, "health benefit"]]},
    {"text": "vitamin E", "entities": [[9, 18, "metabolite"]]},
    {"text": "antiaging", "entities": [[0, 9, "health benefit"]]},
    {"text": "antioxidant", "entities": [[0, 11, "health benefit"]]},
    {"text": "improve visual acuity", "entities": [[0, 21, "health benefit"]]},
    {"text": "protect macula", "entities": [[0, 14, "health benefit"]]},
    {"text": "Lycopene", "entities": [[0, 8, "metabolite"]]},
    {"text": "Lycopene", "entities": [[0, 8, "metabolite"]]},
    {"text": "Vitamin E", "entities": [[0, 9, "metabolite"]]},
    {"text": "Zeaxanthin", "entities": [[0, 10, "metabolite"]]},
    {"text": "Vitamin E", "entities": [[0, 9, "metabolite"]]},
    {"text": "B-carotene", "entities": [[0, 10, "metabolite"]]},
    {"text": "Vitamin E", "entities": [[0, 9, "metabolite"]]},
    {"text": "B-carotene", "entities": [[0, 10, "metabolite"]]},
    {"text": "Lycopene", "entities": [[0, 8, "metabolite"]]},
    {"text": "Lutein", "entities": [[0, 6, "metabolite"]]},
    {"text": "B-carotene", "entities": [[0, 10, "metabolite"]]},
    {"text": "B-carotene", "entities": [[0, 10, "metabolite"]]},
    {"text": "Lycopene", "entities": [[0, 8, "metabolite"]]},
    {"text": "Vitamin E", "entities": [[0, 9, "metabolite"]]},
    {"text": "antiinflamatory", "entities": [[0, 15, "health benefit"]]},
    {"text": "anticancer", "entities": [[0, 10, "health benefit"]]},
    {"text": "anticancer", "entities": [[0, 10, "health benefit"]]},
    {"text": "hepatoprotective", "entities": [[0, 16, "health benefit"]]},
    {"text": "antioxidant", "entities": [[0, 11, "health benefit"]]},
    {"text": "skin diseases", "entities": [[0, 13, "health benefit"]]},
    {"text": "cardiovascular diseases", "entities": [[0, 23, "health benefit"]]},
    {"text": "reduce cataracts", "entities": [[0, 16, "health benefit"]]},
    {"text": "antioxidant", "entities": [[0, 11, "health benefit"]]},
    {"text": "antidiabetic", "entities": [[0, 12, "health benefit"]]},
    {"text": "atherosclerosis disease", "entities": [[0, 23, "health benefit"]]}
]

# Convert the data to spaCy examples. Each training example makes a spaCy Doc object
# It then makes a spaCy Example object from this Doc and the Example object is added to the new_examples list

new_examples = []
for data in new_training_data:
    doc = nlp.make_doc(data["text"])
    example = Example.from_dict(doc, data)
    new_examples.append(example)

# Begin training

nlp.begin_training()

# Set the number of training iterations, this is the number of times it will run through the training data (e.g., 50)

n_iter = 50

# Update the model and drop the losses and print them to ensure that the model is not being overfitted

for itn in range(n_iter):
    losses = {}
    for example in new_examples:
        nlp.update([example], drop=0.5, losses=losses)
    print(losses)

# Save the updated model

nlp.to_disk("ner_model_v6")
