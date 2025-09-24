# Name: Ronak Manoj Maheshwari
# Topic :  Simple AI Chatbot with basic NLP
# Software : Visual Studio Code
# Language : Python


import random
import re

# Dictionary to store intents and responses
intents = {
    "greeting": {
        "patterns": [r"\bhi\b", r"\bhello\b", r"\bhey\b", r"\bgreetings\b", r"how are you"],
        "responses": ["Hello! I'm your friendly chitbot!", "Hi there! Ready to chat?", "Hey! What's up?"]
    },
    "goodbye": {
        "patterns": [r"\bbye\b", r"\bgoodbye\b", r"\bsee you\b", r"\bexit\b", r"\bquit\b"],
        "responses": ["Goodbye! Come back soon!", "See you later!", "Bye bye!"]
    },
    "thanks": {
        "patterns": [r"\bthank you\b", r"\bthanks\b", r"\bappreciate\b"],
        "responses": ["You're welcome!", "No problem!", "Glad to help!"]
    },
    "name": {
        "patterns": [r"what is your name", r"who are you"],
        "responses": ["I'm RM-NLP Bot, nice to meet you!", "My name's ChitBot, what's yours?"]
    },
    "help": {
        "patterns": [r"\bhelp\b", r"what can you do", r"what do you do"],
        "responses": ["I can chat with you! Try saying hi, ask my name, or say thanks. Say 'bye' to exit."]
    },
    "author": {
        "patterns": [r"who developed you", r"what is the name of your developer"],
        "responses": ["My developer's name is Ronak Maheshwari."]
    },
    "weather": {
        "patterns": [r"weather", r"is it raining", r"how's the weather"],
        "responses": ["I'm not a weather app, but I hope it's sunny!", "Weather depends on your location. Carry an umbrella just in case!"]
    },
    "time": {
        "patterns": [r"what time is it", r"tell me the time", r"current time"],
        "responses": ["Time flies when you're chatting! Check your device clock.", "It's always a good time to talk to me!"]
    },
    "learning": {
        "patterns": [r"how to learn python", r"best way to learn coding", r"suggest learning resources"],
        "responses": ["Start with freeCodeCamp, W3Schools, or Codecademy!", "Practice daily and build small projects. You'll get there!"]
    },
    "funny": {
        "patterns": [r"tell me a joke", r"make me laugh", r"say something funny"],
        "responses": ["Why did the computer get cold? Because it left its Windows open!", "I would tell you a joke about UDP... but you might not get it."]
    },
    "philosophy": {
        "patterns":[r"what is meaning of life",r"why do we exist",r"is there a purpose of living"],
        "responses": ["To learn, grow, and maybe chat with bots like me","That's a deep question.Even I am still processing"]
    },
    "ai": {
        "patterns": [r"are you intelligent", r"do you think", r"can you feel emotions"],
        "responses": ["I'm smart enough to chat, but emotions? Still working on that!", "I think in code, not feelings.", "I simulate intelligence, but you're the real thinker here."]
    },
    "riddles": {
        "patterns": [r"tell me a riddle", r"give me a puzzle", r"challenge me"],
        "responses": ["What has keys but can't open locks? A piano!", "I speak without a mouth and hear without ears. What am I? (Answer: An echo)", "The more you take, the more you leave behind. What are they? (Answer: Footsteps)"]
    },
    "facts": {
        "patterns": [r"tell me a fact", r"interesting fact", r"did you know"],
        "responses": ["Did you know honey never spoils? Archaeologists found 3,000-year-old honey in Egyptian tombs!", "Octopuses have three hearts. That’s a lot of love!", "Bananas are berries, but strawberries aren’t. Weird, right?"]
    },
    "games": {
        "patterns": [r"can we play a game", r"play something", r"game time"],
        "responses": ["I love games! Try guessing a number between 1 and 10.", "Let’s play a word association game. You say a word, I’ll respond!", "I’m not a console, but I can keep you entertained!"]
    }

    
}


# Function to preprocess user input
def preprocess_input(user_input):
    # Convert to lowercase and remove extra spaces
    user_input = user_input.lower().strip()
    # Remove punctuation
    user_input = re.sub(r'[^\w\s]', '', user_input)
    return user_input

# Function to match user input to an intent
def get_intent(user_input):
    user_input = preprocess_input(user_input)
    
    # Check each intent and its patterns
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if re.search(pattern, user_input):
                return intent, random.choice(data["responses"])
    
    # Default response if no intent matches
    return None, "Sorry, I didn't understand that. Try saying 'help' for options!"

# Main chatbot function
def chatbot():
    print("Welcome to GrokBot! Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Get intent and response
        intent, response = get_intent(user_input)
        
        # Print response
        print("GrokBot:", response)
        
        # Check if user wants to exit
        if intent == "goodbye":
            break

# Run the chatbot
chatbot()


#Explaination :
#This Python script builds a conversational AI chatbot named ChitBot using basic natural language processing techniques.
# ChitBot operates on a rule-based system where user inputs are matched against predefined patterns using regular expressions.
# These patterns are grouped under various "intents" such as greetings, farewells, help requests, thanks, jokes, and riddles.
# Each intent contains a list of regex patterns representing possible user queries and a corresponding list of responses.
# When a user types a message, the chatbot first preprocesses the input by converting it to lowercase.
# It also removes punctuation to ensure consistent matching across different variations of user input.
# The chatbot then checks the input against all patterns in the intents dictionary to find a match.
# If a match is found, the bot randomly selects a response from the relevant intent and displays it.
# If no match is found, it replies with a default message indicating it didn’t understand the input.
# The chatbot runs in a loop, continuously accepting user input until the user types a goodbye intent.
# Goodbye intents include phrases like "bye" or "exit," which break the loop and end the conversation.
# The output is interactive and varied—for example, typing “hello” might trigger a cheerful greeting.
# Typing “tell me a joke” could return a tech-themed punchline, adding humor to the interaction.
# Newly added intents make the chatbot more engaging by responding to philosophical questions and fun facts.
# For instance, it can answer “what is the meaning of life” or share facts like “bananas are berries.”
# It can also challenge users with riddles or play simple games, making the experience more dynamic.
# This structure makes ChitBot a great example of combining simple logic and creativity in chatbot design.
# It’s ideal for beginners exploring NLP and chatbot development using Python and regular expressions.
# The project lays the groundwork for more advanced features like fuzzy matching and machine learning classification.
# Future enhancements could include integrating APIs for real-time data or using NLP libraries like spaCy.
# You could also add sentiment analysis or context tracking to make the bot more intelligent and responsive.
# The rule-based design is easy to understand and modify, making it perfect for educational or demo purposes.
# Each intent is modular, allowing developers to expand the bot’s capabilities with minimal effort or complexity.
# The use of regex allows flexible pattern matching, though it may struggle with ambiguous or complex queries.
# Despite its simplicity, ChitBot demonstrates core NLP concepts like tokenization, intent recognition, and response generation.
# It’s a fun and functional chatbot that showcases how basic tools can create meaningful user interactions.