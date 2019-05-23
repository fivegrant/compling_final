#!/usr/bin/env python3
import dependencies, mod, mispeller
import sys

input = sys.argv[1]
extension = sys.argv[2]

wrong = mispeller.Mispeller()
processor = mod.Word_Modifier(input)
print(processor.apply(wrong.mispell, extension))

