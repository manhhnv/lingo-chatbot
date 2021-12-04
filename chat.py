from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Ron Obvious")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "I am chatter bot."
    "My name is chatter bot."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response("What is your name?")
print(response)
