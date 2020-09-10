from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_first_response
from treinador_chatbot import treinar, padroniza
from adapters import adapters
from preprocessors import preprocessors
from return_resposta_especifica import resposta_especifica
import logging

#logging.basicConfig(level=logging.INFO)

botOcomon = ChatBot('botOcomon', read_only = True, preprocessors = preprocessors(), logic_adapters = adapters(LevenshteinDistance, get_first_response))

#treinar(botOcomon)

inicio = True
while True:
    if inicio == True:
        try:
            resposta = resposta_especifica(botOcomon)
            print('BotOcomon: {}'.format(resposta))
            inicio = False
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
    else:
        try:
            pergunta = input('Humano: ')
            pergunta = padroniza(pergunta)
            resposta = botOcomon.get_response(pergunta)
            if resposta.confidence > 0 and resposta.confidence <= 0.50:
                print('BotOcomon: {}'.format('Olá, sou o Ocomon. Para que eu possa te ajudar, envie perguntas do tipo "Anunciar Oportunidade de Bolsa".'))
            else:
                print('BotOcomon: {}'.format(resposta))
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
