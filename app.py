import json

data = json.load(open("data.json"))


def translate(word):
    try:
        return data[word.lower()]
    except:
        return "The word does not exist. Please double check it!"


word = input("Enter the word:")
print(translate(word))
