import sys
import pprint
from gensim import corpora

try:
    xrange
except NameError:
    xrange = range

pp = pprint.PrettyPrinter()

def get_dictionary(fname, max_vocabulary_size)
  with open(fname) as f:
    texts = [word for word in f.read().lower().split()]
    return corpora.Dictionary([texts], prune_at=max_vocabulary_size)
