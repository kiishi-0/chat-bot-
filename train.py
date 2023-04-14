import json

with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags=[]
xy=[]
print(intents['intents'][6])
# for intent in intents['intents']:
#     tag = intent['tag']
#     tags.append(tag)
#     for pattern in intent['patterns']:
#         patterns.append(pattern)