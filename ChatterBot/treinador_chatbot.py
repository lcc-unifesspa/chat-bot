from chatterbot.trainers import ListTrainer
import pandas as pd
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer

stemming = SnowballStemmer(language = 'portuguese')

def padroniza(frase):

    ignorar = ['?', '.', '!', ',', '[', ']', '(', ')', 'a', 'de',
               'o', 'da', 'que', 'e', 'do', 'R$', '$', 'US$', 'kg', 'km', 'milhões', 'bilhões']

    frase = frase.lower()
    frase = word_tokenize(frase)

    frase_nova = ''

    for palavra in frase:
        if palavra not in ignorar:
            #palavra = stemming.stem(palavra)
            frase_nova = frase_nova + palavra + ' '

    return frase_nova

def treinar(bot):
    df = pd.read_csv('dataset.csv')
    treinador = ListTrainer(bot)
    for linha in range( df.shape[0] ):
        treinador.train([padroniza(df.iloc[linha, 0]), df.iloc[linha, 1]])

