# Script installs all dependencies
import sys, io, os, subprocess

# Ensures the download is silent if this file is treated as a module.
if __name__ != '__main__':
    sys.stdout = io.StringIO()
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'nltk'])
    from nltk import *
    download('cmudict')
    download('words')
    sys.stdout = sys.__stdout__

else:
    print("Installing Dependencies:")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'nltk'])
    from nltk import *
    download('cmudict')
    download('words')

# Sources
## In-code pip
###https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program
## Hiding the prints
### https://stackoverflow.com/questions/8391411/suppress-calls-to-print-python
   


