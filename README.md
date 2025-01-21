# AI-CHATBOT-WITH-NLP

**COMPANY** : CODETECH IT SOLUTIONS

**NAME** : ANIKET KUMAR PRASAD

**INTERN ID** : CT12WLSO

BATCH DURATION : January 10th, 2025 to April 10th, 2025

**MENTOR NAME** : Neela Santhosh

# DESCRIPTION OF PROJECT

Project Title: **AI Chatbot with NLP**

**Overview:**
This project demonstrates the creation of an AI chatbot using Natural Language Processing (NLP) techniques with the NLTK (Natural Language Toolkit) library in Python. The chatbot can respond to basic queries and carry on conversations with the user. It is capable of answering simple questions about itself and providing predefined responses based on user inputs. This project highlights how NLP can be used to make a bot understand and respond to user queries in a meaningful way.

The chatbot uses pattern matching to identify user queries and provide appropriate responses. The use of regular expressions helps the bot recognize a wide range of inputs and respond accordingly. It is an excellent introduction to building conversational AI applications.

**Key Features:**
- The chatbot can initiate conversations and greet the user.
- It can respond to queries like "What is your name?" or "What is NLP?"
- The chatbot can handle invalid or unrecognized inputs with predefined responses.
- The chatbot can be exited by typing "quit".

**Tools and Libraries Used:**
- **Python**: The programming language used to develop the chatbot.
- **NLTK (Natural Language Toolkit)**: A powerful library used for handling NLP tasks such as tokenization, stemming, and pattern matching.
- **Regular Expressions (Regex)**: Used for pattern matching in user inputs to find the relevant responses.
- **Reflections**: A feature of NLTK to handle simple input-output mappings (e.g., replacing “I” with “You”).

**Explanation of Code:**
The chatbot uses a list called pairs that contains patterns (regular expressions) and corresponding responses. These pairs define how the chatbot should react to user inputs. If the user inputs a query that matches one of the patterns, the chatbot will respond with one of the predefined responses.

Here’s how the key parts of the code work:
- **Patterns and Responses**: Each pattern matches a particular type of user input. The chatbot responds based on these patterns. For example, if the user types "hi" or "hello", the bot will greet them with one of the responses like "Hi there" or "Hi, how can I help?"
- **The Chat Class**: The Chat class from NLTK is used to initialize the chatbot with the patterns and responses. It processes user input and returns the appropriate response.
- **User Interaction**: The chatbot runs in a continuous loop until the user types "quit". During the conversation, it listens for user inputs, checks for matches with predefined patterns, and responds accordingly.

**Sample Interactions:**
- User: "Hi"
  - Chatbot: "Hi there"
- User: "What is NLP?"
  - Chatbot: "Natural language processing (NLP) is the discipline of building machines that can manipulate human language — or data that resembles human language — in the way that it is written, spoken, and organized."
- User: "Quit"
  - Chatbot: "Thanks for chatting! Have a great day ahead!"

**Output:**
The output of this project is a functional chatbot that interacts with users based on predefined patterns. The chatbot responds with simple, meaningful answers to a set of queries. It can continue the conversation until the user types "quit", upon which the chatbot says goodbye and exits.

**Resources Used:**
- **NLTK Documentation**: The official documentation helped understand how to use the Chat class and regular expressions for building a conversational chatbot.
- **W3Schools**: Provided a solid understanding of Python basics and regular expressions.
- **YouTube Tutorials**: These were useful for learning how to integrate NLP techniques into building interactive chatbots.
- **ChatGPT**: For helping understand how and why things works this way, for clarity.

This chatbot serves as a basic example of NLP in action, demonstrating how natural language can be processed and understood by machines, even in simple use cases.

# OUTPUT OF THE TASK

![Image](https://github.com/user-attachments/assets/a794b09d-ca64-443c-aec7-f27d25f97981)
