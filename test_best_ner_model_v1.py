import spacy
from PyQt5.QtWidgets import QApplication, QInputDialog

# Load your NER model
nlp = spacy.load("best_ner_model_v1")

app = QApplication([])

# Get user input from a pop-up dialog box
user_input, ok = QInputDialog.getText(None, "Input", "Enter your text:")

# Define a list of common words to filter out
common_words = ["making", "which", "it", "is", "also", "its", "some", "that", "can", "you",
                "like", "may", "of", "be", "this", "by", "&", "the", "and",
                "or", "a", "an", "in", "on", "at", "to", "for", "with", "as",
                "from", "while", "are", "thus", "such", "include", "including", "present",
                "these", "will", "Therefore", "therefore", "they" "associated", "tomato", "tomatoes",
                "carrot", "carrots", "mainly", "associated", "other", "addition", "previously",
                "important", "Additionally", "additionally", "different", "abundant", "Abundant", "main",
                "They"]

def process_word(word):
    # Process the word
    doc = nlp(word)
    
    # Check if the word is a metabolite or health benefit
    if doc[0].ent_type_ in ['metabolite', 'health benefit']:
        print(f"Entity: {word}, Label: {doc[0].ent_type_}")

if ok:
    # Remove commas and split the input into words
    words = user_input.replace(',', '').split()
    
    # Process each word
    for word in words:
        if word.lower() not in common_words:
            process_word(word)
