import json
from difflib import get_close_matches

data = json.load(open("076 data.json"))


def translate(word):

    word = word.capitalize()
    if word in data is not None:   
        return data[word]
    
    word = word.upper()
    if word in data is not None:   
        return data[word]
    


    word = word.lower()
    if word in data is not None:   
        return data[word]

    
    elif len(get_close_matches(word, data.keys()))>0:
        x=input("Did you mean %s instead. Yes:y \n No: n \n"%get_close_matches(word,data.keys())[0])
        
        if x=="y":
            
            print(translate(get_close_matches(word,data.keys())[0]))
            return "Thanks for Using KKCDIctionary"
        elif x=="n":
            return "The word doesn't exist, double check it"
        else :
            return "we didn't understand your query."

    else:
        return "The word doesn't exist. Please double check it "


word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

