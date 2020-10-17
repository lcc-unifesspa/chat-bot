from chatterbot.trainers import ListTrainer
import pandas as pd
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
df = pd.read_csv('dataUpdate.csv')
for linha in range(df.shape[0]):
    print([(df.iloc[linha, 0]), df.iloc[linha, 1]])
