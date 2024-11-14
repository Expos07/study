def convert_abbreviations(message):
    words = message.split(" ")
    abbreviations = {
        "brb": "be right back",
        "gtg": "got to go",
        "lol": "laugh out loud",
        "idk": "I don't know"
    }
    output = ""
    for word in words:
        output += abbreviations.get(word, word) + " "
    return output.strip()

messages = input(">")
print(convert_abbreviations(messages))