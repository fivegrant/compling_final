#!/usr/bin/env python3
import mod, misspeller, unmisspeller
import sys

if 'init' in sys.argv:
    import dependencies
    
input = sys.argv[1]

processor = mod.Word_Modifier(input)

wrong = misspeller.Misspeller()
processor.apply(wrong.misspell, 'bad')

#More right than wrong hence 'wright'
wright = unmisspeller.UnMisspeller()
processor.apply(wright.wrong_words, 'kinda_bad')


