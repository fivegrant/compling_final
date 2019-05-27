# MODULES: "nltk"
# NLTK DOWNLOADS: "words", "cmudict"

from nltk.corpus import cmudict
import nltk, re

class Misspeller:
    def __init__(self):
        self.pronounce = cmudict.dict()
        self.real_words = nltk.corpus.words.words()

    def misspell(self, word):
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

