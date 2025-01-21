# AI CHATBOT WITH NLP

import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
# [r"queries",[responses]]

pairs = [
    # initiating conversation
    [r"hi|hello|hey|hola",["hi there", "hi", "hi, how are you?", "hi how can i help?"]],
    
    # asking name
    [r"what are you|who are you|what is your name|name|whats your name",["I dont have a name, i am a NLP chatbot", "I am bot"]],
    
    # asking question
    [r"nlp|what is nlp",["Natural language processing (NLP) is the discipline of building machines that can manipulate human language — or data that resembles human language — in the way that it is written, spoken, and organized.","Natural language processing (NLP) is a subfield of computer science and especially artificial intelligence. \n Go to this link to know more - https://en.wikipedia.org/wiki/Natural_language_processing"]],
    
    # To quit
    [r"quit", ["Thanks for chatting! Have a great day ahead!", "Goodbye! Take care."]],
    
    # For some invalid input
    [r"(.*)", ["I dont know", "I dont understand understand.", "Not yet programmed for doing that"]]
]

# Creating object of chat class to make chatbot
chatbot = Chat(pairs, reflections)

# Using chatbot
print("Chatbot: Hi! Type 'quit' to exit.")
while True:
    user_input = input("\n\nYou: ").lower()
    if user_input == "quit":
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot.respond(user_input))

