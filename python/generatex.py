# Generate sentences from a grammar
# Based on code from Adam

from nltk import grammar, parse, load_parser
import sys
# import itertools
# import random

#from nltk.parse.generate import generate
#from nltk.probability import FreqDist
#from nltk import CFG
#from nltk import grammar

grammar_file = sys.argv[1]
x_sentence = sys.argv[2].split()
#probability = float(sys.argv[3])
#N = int(sys.argv[4])

print(grammar_file)
print(x_sentence)

pr = load_parser(grammar_file, trace=0,cache=False)

itr = pr.parse(x_sentence)

tr1 = next(itr)

print(tr1)

#for i in range(N):
#  print(next(itr))

  




