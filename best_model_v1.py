import spacy
from spacy.training.example import Example
import ast

nlp = spacy.load("best_ner_model_v1")  # Load your existing model
ner = nlp.get_pipe("ner")

# Read the data from the text file
with open("ALL_metabolites_health_v1.txt", 'r', encoding='utf-8') as file:
    new_training_data = ast.literal_eval(file.read())

new_examples = []
for data in new_training_data:
    doc = nlp.make_doc(data["text"])
    example = Example.from_dict(doc, data)
    new_examples.append(example)

# Set the number of training iterations (e.g., 10)
nlp.begin_training()
n_iter = 50

best_loss = float('inf')  # Initialize best loss to a high value
patience = 5  # Define a patience threshold

for itn in range(n_iter):
    losses = {}
    for example in new_examples:
        try:
            nlp.update([example], drop=0.5, losses=losses)
        except Exception as e:
            pass  # Skip examples with errors (likely misaligned entities)
    
    current_loss = losses.get('ner', float('inf'))  # Get current NER loss
    print(f"Iteration {itn+1}, NER Loss: {current_loss}")
    
    if current_loss < best_loss:
        best_loss = current_loss
        # Save the best model
        nlp.to_disk("best_ner_model_v1")
        patience = 5  # Reset patience if a new best loss is found
    else:
        patience -= 1
    
    if patience == 0:
        print("Early stopping. No improvement in validation loss.")
        break
