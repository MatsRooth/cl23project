# Generate sentences from a grammar
# Based on code from Adam

import sys
import itertools
import random
from nltk.parse.generate import generate
from nltk.probability import FreqDist
from nltk import CFG
from nltk import grammar



def gen_words(grammar, n, p, d):
    for sentence in generate(grammar, depth=d):
        if len(sentence) == n:
            if random.random() < p:
                yield sentence
            else:
                continue
            
grammar_file = sys.argv[1]
sentence_length = int(sys.argv[2])
depth = int(sys.argv[3])
probability = float(sys.argv[4])
N = int(sys.argv[5])

with open(grammar_file, 'r') as file:
    gstring = file.read()

g = grammar.FeatureGrammar.fromstring(gstring)
    
sen_gen = gen_words(g, sentence_length, probability, depth)

for i in range(N):
  print(" ".join(next(sen_gen)))



