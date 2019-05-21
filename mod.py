import nltk
import re

class Word_Modifier:
    def __init__(self, input_file):
        self.input_name = input_file 
        self.data = []
        with open(input_file, 'r') as file:
            self.data = nltk.word_tokenize(file.read())

    def apply(self, process, end):
        output = ''
        processed = map(process, self.data)

        hold = ''
        for word in processed:
            if re.match(r"""[.!;?"',]""", word):
                hold += word
            elif len(hold + ' ' + word) < 80:
                hold += ' ' + word
            else:
                hold += '\n'
                output += hold
                hold = ''
        output += hold
            
        with open(self.input_name + '.' + end, 'w') as file:
            file.write(output)

        return output

if __name__ == '__main__':
    def st(a):
        return a
    w = Word_Modifier('tap')
    w.apply(st, 'output')

