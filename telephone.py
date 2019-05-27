#!/usr/bin/env python3
import dependencies, mod, mispeller
import sys

input = sys.argv[1]

wrong = mispeller.Mispeller()
processor = mod.Word_Modifier(input)
print(processor.apply(wrong.mispell, 'bad'))

