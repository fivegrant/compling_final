# Compling Final
This project takes a file and returns two.

The first returned file will be phonetically
identical to the input, however, every word 
will be misspelled. 

The second returned file will return the 
input file but with the words that have a
phonetically identical twin are substituted.

## Usage
If it's the first time you're running it, run:
`./telephone.py input_file init` to make sure the proper files
are installed. Any other execution of the script after the initial
run can be formatted as `./telephone.py input_file`

Output will be `input_file.bad` for the misspelled
file and `input_file.kinda_bad` for the similar 
words file.

## Structure
Four modules alongside `telephone.py` make up this
project: 
`mod.py`,`misspeller.py`,`unmisspeller.py`, `dependencies.py`

### Quick overview of what each module does
- `dependencies.py` is similar to a `requirements.txt`,
however, all of the installation is done automatically.
- `mod.py` takes a function and maps it to every token. Then
it writes an output file that does not write more than 80
characters per line.
- `misspell.py` takes a word and returns the phonemes combined
into one string
- `unmisspell.py` reverses the CMU Dictionary to take a combined
list of phonemes and return a word instead. `unmisspell.py`
contains a Misspell object which converts a word to phonemes
before being converted back to a word again. The original word
is returned if there are no identical phonemes.

## Justin's Evaluation Criteria

### "If it runs / does what you say it does"
- Does what it was intended to do. See above.
### "If it uses any tools/techniques/algorithms covered in class"
- The project uses regular expressions to clean some of the phoneme data
and word processing data.
- Word tokenization is incorporated to break down text.
- NLTK Packages are used.
- If the project were to be extended, it would implement word vectors
to use the Misspeller and UnMisspeller to create puns.
### "The code organization and clarity"
- Everything is modular to allow for parts to be added or removed.
- Object Oriented Approach keeps everything clean.
- `dependency.py` ensures the code will run on any machine with python 3
### "How much effort you put into it"
The effort spent on this work went to the following tasks:
- Understanding CMU Dict
- Figuring out the word processor
- Structuring the Misspeller, Word_Modifier, and UnMispeller components to 
fit together.
- Creating the UnMisspeller
- Debugging


## CMU Dict
- http://www.nltk.org/_modules/nltk/corpus/reader/cmudict.html
- http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in=bubonic
