import os
from gensim import corpora

def get_dictionary(fname, max_vocabulary_size=None):
  with open(fname) as f:
    texts = [word for word in f.read().lower().split()]
    return corpora.Dictionary([texts], prune_at=max_vocabulary_size)

class Loader(object):

  def __init__(self, dataset, batch_size, dataset_dir="data", 
               title_fname="title.txt", article_fname="article.txt"):
    self.dataset = dataset
    self.batch_size = batch_size
    self.dataset_dir = dataset_dir

    title_fname = os.path.join(self.dataset_dir, self.dataset, title_fname)
    articles_fname = os.path.join(self.dataset_dir, self.dataset, article_fname)

    self.article_dict = get_dictionary(title_fname)
    import ipdb; ipdb.set_trace() 
