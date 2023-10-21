#import required libraries

import spacy
from spacy.training.example import Example
import ast

#load previously trained model, this is a model that is based off the initial training explained in the appendices

nlp = spacy.load("best_ner_model_v1")  # Load your existing model

#get ner component from the spaCy pipeline

ner = nlp.get_pipe("ner")

#read the data from the text file that includes all metabolites and health benefit data combined

with open("ALL_metabolites_health_v1.txt", 'r', encoding='utf-8') as file:
    new_training_data = ast.literal_eval(file.read())

#processed training examples were stored in new_examples

new_examples = []

#for loop that iterated through the new_training_data, where a spaCy doc object is created, 
#this is needed to create the training example

for data in new_training_data:
    doc = nlp.make_doc(data["text"])
    example = Example.from_dict(doc, data)
    new_examples.append(example)

#begin training the model with the input data

nlp.begin_training()

#set the iterations for how many times the model will be trained through the input data

n_iter = 50

#start the best loss at a high value

best_loss = float('inf')

#patience threshold is defined to 5

patience = 5

#for loop to start the iterative training process

for itn in range(n_iter):
    losses = {}
    for example in new_examples:
        try:
            nlp.update([example], drop=0.5, losses=losses)

#except statement to catch any exceptions during the training
            
        except Exception as e:
            pass  # pass or skip examples with errors (likely misaligned entities)

#define current losses and print these losses
    
    current_loss = losses.get('ner', float('inf'))  # Get current NER loss
    print(f"Iteration {itn+1}, NER Loss: {current_loss}")

#if/else statements that will stop training if the patience threshold is not within specification
#this will prevent overfitting of the model to ensure the most accurate training of model
    
    if current_loss < best_loss:
        best_loss = current_loss
#save the best model
        nlp.to_disk("best_ner_model_v1")
        patience = 5  # Reset patience if a new best loss is found
    else:
        patience -= 1
    
    if patience == 0:
        print("Early stopping. No improvement in validation loss.")
        break
