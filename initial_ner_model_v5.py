#import appropriate libraries to execute the code

import spacy
from spacy.training.example import Example

#load existing model
#ner_model_v4 has minimal training, this model was a test model to ensure python program was executed correctly

nlp = spacy.load("ner_model_v4")

#get ner componenent from the spaCy pipeline

ner = nlp.get_pipe("ner")

#assign the training data to new_training_data in prep to be fed into training the model

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
]

#processed training examples were stored in new_examples

new_examples = []

#for loop that iterated through the new_training_data, where a spaCy doc object is created, this is needed to create the training example

for data in new_training_data:
    doc = nlp.make_doc(data["text"])
    example = Example.from_dict(doc, data)
    new_examples.append(example)

#begin training the model with the input data

nlp.begin_training()

#set the iterations for how many times the model will be trained through the input data

n_iter = 50

#for loop to start the iterative training process

for itn in range(n_iter):
    losses = {}
    for example in new_examples:

#define current losses and print these losses
        
        nlp.update([example], drop=0.5, losses=losses)
    print(losses)

#save the updated model
    
nlp.to_disk("ner_model_v5")
