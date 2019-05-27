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
            pronunciation = self.pronounce[word]
        except:
            return word
        else:
            for possible in pronunciation:
                content = ''.join(possible)
                content = re.sub(r'\d', r'', content)

                if content not in self.real_words:
                    return content
                word = content
            return word

