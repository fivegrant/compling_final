import sys, subprocess, os

print("Installing Dependencies:")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'nltk'])
from nltk import *
download('cmudict')
download('words')



