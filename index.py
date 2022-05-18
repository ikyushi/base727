from json import *

letters = json.load(open('letters.json', 'r'))

def split(word):
    # from geeksforgeeks
    return [char for char in word]

message = input("What's your original message? ")
while True:
    correct = input("Your message is '%s'. Is this correct? (Y/n)" % message)
    if correct = "" or "y":
        return message = message
        break
    message = input("What's your original message? ")

print("Encoding...")
splitmessage = split(word=message).lower()
encoded = []

for x in splitmessage:
    encoded.append(letters[x])

print("Your encoded message is: '%s" % encoded)
print("To use this program again, just restart the app.+")