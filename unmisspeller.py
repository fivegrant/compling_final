# MODULES: "nltk"
# NLTK DOWNLOADS: , "cmudict"

from nltk.corpus import cmudict
import nltk, re
import misspeller

class UnMisspeller:
    def __init__(self):
        pronounce = cmudict.dict()
        self.phonetic_map = {}
        self.misspeller = misspeller.Misspeller()
        for word, possible_list in pronounce.items():
            for possible in possible_list:
                content = ''.join(possible)
                content = re.sub(r'\d', r'', content)
                if content not in self.phonetic_map:
                    self.phonetic_map.update({content:[word]})
                else:
                    self.phonetic_map[content].append(word)

    def fix(self, phonemes):
        phonemes = phonemes.upper()
        try:
            word_list = self.phonetic_map[phoneme]
        except:
            return phonemes
        else:
            for possible_word in word_list:
                return possible_word

    def wrong_words(self, word):
        misspelled = self.misspeller.misspell(word)
        try:
            word_list = self.phonetic_map[misspelled]
        except:
            return misspelled
        else:
            catch = ''
            for possible_word in word_list:
                catch = possible_word
                if possible_word != word: 
                    return possible_word
            return catch



        
            
