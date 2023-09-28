import spacy
from spacy.training.example import Example

nlp = spacy.load("ner_model_v5")  # Load your existing model
ner = nlp.get_pipe("ner")

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
        nlp.update([example], drop=0.5, losses=losses)
    print(losses)

# Save the updated model
nlp.to_disk("ner_model_v6")
