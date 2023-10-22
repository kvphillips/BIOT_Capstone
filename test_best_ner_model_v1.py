import spacy
from PyQt5.QtWidgets import QApplication, QInputDialog

#load the finalized NER model
nlp = spacy.load("best_ner_model_v1")

app = QApplication([])

#user input and copy/pasted text is collected from a pop-up dialog box
user_input, ok = QInputDialog.getText(None, "Input", "Enter your text:")

#model is setup to label entire sentences, therefore this will remove output words that are commonly mislabelled within the sentence
#and add no value to the data ouptput
common_words = ["making", "which", "it", "is", "also", "its", "some", "that", "can", "you",
                "like", "may", "of", "be", "this", "by", "&", "the", "and",
                "or", "a", "an", "in", "on", "at", "to", "for", "with", "as",
                "from", "while", "are", "thus", "such", "include", "including", "present",
                "these", "will", "Therefore", "therefore", "they" "associated", "tomato", "tomatoes",
                "carrot", "carrots", "mainly", "associated", "other", "addition", "previously",
                "important", "Additionally", "additionally", "different", "abundant", "Abundant", "main",
                "They"]

def process_word(word):
#process each word with the NLP model
    doc = nlp(word)
    
#check if the word is a metabolite or health benefit and print the output entity and label
    if doc[0].ent_type_ in ['metabolite', 'health benefit']:
        print(f"Entity: {word}, Label: {doc[0].ent_type_}")

if ok:
#remove additional special characters like commas and split the input into words
    words = user_input.replace(',', '').split()

#process each word in prep to be fed into the mode
    for word in words:
        if word.lower() not in common_words:
            process_word(word)
