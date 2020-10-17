from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Create a new ChatBot with name Dev.to
chatbot = ChatBot(
    'Dev.to',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)

chatbot = ChatBot("Dev.to")
chatbot.storage.drop()
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)


trainer.train(
    "chatterbot.corpus.portuguese.greetings"
)
# Train the chatbot based on the english corpus

print("\nHello i'm Dev.to Bot\n")
while True:
    try:
        bot_input = input()

        if bot_input.strip()=='Stop':
            print('Dev.to: Bye')
            break

        bot_response = chatbot.get_response(bot_input)
        print(bot_response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
