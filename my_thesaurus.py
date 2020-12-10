import json
from difflib import get_close_matches
data = json.load(open("thesaurus/data.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        confirm = input("Did you mean %s? Type Y if yes and N if no: " %get_close_matches(w, data.keys())[0])
        if confirm == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif confirm == 'N':
            return "The word doesn't exist. Please retry."
        else:
            return "Your response was invalid. Please try again."
        
    else:
        return "Word doesn't exist. Please retry."
word= input("Enter a word: ")
output= translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)