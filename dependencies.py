# Script installs all dependencies
import sys, os, subprocess

# Ensures the download is silent if this file is treated as a module.
if __name__ != '__main__':
    original_state = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'nltk'])
    from nltk import *
    download('cmudict')
    download('words')
    sys.stdout.close()
    sys.stdout = original_state

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
   


