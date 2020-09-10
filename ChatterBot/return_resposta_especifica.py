from datetime import datetime

def resposta_especifica(bot):

    if datetime.now().hour >= 6 and datetime.now().hour <= 12:
        resposta = bot.get_response('manha')
    elif datetime.now().hour > 12 and datetime.now().hour <= 18:
        resposta = bot.get_response('tarde')
    elif datetime.now().hour > 18 and datetime.now().hour <= 23:
        resposta = bot.get_response('noite')
    else:
        resposta = bot.get_response('saudacoes')

    return resposta

