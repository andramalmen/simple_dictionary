import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    try:
        return data[word.lower()]
    except Exception as err:
        closeMatches = get_close_matches(word, data.keys(), n=1)
        if len(closeMatches) == 0:
            return "The word does not exist. Please double check it!"
        else:
            response = input(
                'Did you mean "%s"? Enter Y for yes and N for no ' %
                closeMatches[0])
            if response == "Y":
                return data[closeMatches[0]]
            elif response == "N":
                return "The word does not exist. Please double check it!"
            else:
                return "Option not available"


word = input("Enter the word:")
print(translate(word))
