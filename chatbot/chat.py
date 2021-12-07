from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chat_bot = ChatBot("lingo-chatterbot")

trainer = ChatterBotCorpusTrainer(chat_bot)
trainer.train("data/data.yml")

while True:
    try:
        user_input = input()

        bot_response = chat_bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
