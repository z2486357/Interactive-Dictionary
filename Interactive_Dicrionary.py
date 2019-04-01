import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def meaning (input_word):
    if input_word in data.keys():
        return data[input_word]
    elif input_word.title() in data.keys():
        return data[input_word.title()]
    elif input_word.upper() in data.keys():
        return data[input_word.upper()]
    elif input_word.lower() in data.keys():
        return data[input_word.lower()] 
    elif len(get_close_matches(input_word,data.keys(),n=1,cutoff=0.7))!=0:
        most_related=get_close_matches(input_word,data.keys(),n=1,cutoff=0.7)[0]
        YorN=input("Did you mean %s ? Type Y for Yes and N for No : " % most_related)
        YorN=YorN.upper()
        if YorN == "Y":
            return data[most_related]
        elif YorN == "N":
            return ["Doesn't find. Check again!"]
        else:
            print("Meaningless input, follow is the meaning of \"%s\":" %most_related)
            return data[most_related]
    else:
        return ["Doesn't find. Check again!"]

user_input=input("Enter the word: ")
output=meaning(user_input)
for i in output:
    print(i)


