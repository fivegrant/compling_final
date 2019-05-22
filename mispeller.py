try:
    nltk.download('cmudict')
except:
    pass
try:
    nltk.download('corpus')
except:
    pass
try:
    nltk.download('words')
except:
    pass

from nltk.corpus import cmudict
import nltk
import mod

class Mispeller:
    def __init__(self):
        self.pronounce = cmudict.dict()
        self.real_words = nltk.corpus.words.words()

    def mispell(self, word):
        word = self.pronounce[word]
        word = ''.join(word)
        word = word.replace(['1','2','3','4','5','6','7','8','9','0'],'')
        return word

if __name__ == "__main__":
    test = Mispeller()
    print(test.mispell('word'))
    print(test.mispell('sentence'))
    print(test.mispell('cruel'))
