# MODULES: "nltk"
# NLTK DOWNLOADS: "words", "cmudict"

from nltk.corpus import cmudict
import nltk, re
import mod

class Mispeller:
    def __init__(self):
        self.pronounce = cmudict.dict()
        self.real_words = nltk.corpus.words.words()

    def mispell(self, word):
        word = word.lower()
        try:
            pronouciation = self.pronounce[word]
        except:
            return word
        else:
            for possible in pronouciation:
                possible = ''.join(possible)
                possible = re.sub(r'\d', r'', possible)

                if possible not in self.real_words:
                    return possible
                word = possible
            return word

