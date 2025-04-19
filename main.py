# Import spacy 
import spacy
from spacy.matcher import PhraseMatcher

# Load English tokenizer, tagger, parser and NER
# python -m spacy download en_core_web_sm 
nlp = spacy.load("en_core_web_sm")

# Define categories and associated phrases
hardware = ["keyboard", "mouse", "laptop", "monitor", "printer"]
software = ["install", "crash", "update", "license", "application"]
general_enquiry = ["how to", "help", "support", "question", "inquiry"]

hardware_patterns = [nlp(h) for h in hardware]
software_patterns = [nlp(s) for s in software]
ge_patterns = [nlp(ge) for ge in general_enquiry]

# Initialize the PhraseMatcher
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# pass pattern lists to phrase matcher
matcher.add("HARDWARE_pattern", hardware_patterns)
matcher.add("SOFTWARE_pattern", software_patterns)
matcher.add("GE_pattern", ge_patterns)

# Example ticket texts
tickets = [
    "My laptop screen is flickering",
    "How do I install the new software update?",
    "I have a question about billing",
    "The printer is not working",
    "The app keeps crashing"
]

for ticket in tickets:
    doc = nlp(ticket)
    matches = matcher(doc)
    categories = set([nlp.vocab.strings[match_id] for match_id, start, end in matches])
    print(f'"{ticket}" category is: {", ".join(categories) if categories else "Uncategorized"}')
    
    
    