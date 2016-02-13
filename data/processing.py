#!/bin/python
import os
import sys
import json

input_path = sys.argv[1]

title_path = os.path.join(os.path.dirname(input_path), "title.txt")
article_path = os.path.join(os.path.dirname(input_path), "article.txt")

with open(input_path) as f,
     open(title_path, "w") as t_f,
     open(article_path, "w") as a_f:
  for item in json.loads(f):
    title, article = item['t'], item['a']

    title_words = title.strip().split()
    article_words = article.strip().split()

    # No blanks.
    if any((word == "" for word in title_words)):
      continue

    if any((word == "" for word in article_words)):
      continue

    if not any((word == "." for word in article_words)):
      continue

    bad_words = []

    if any((bad in title.lower()
        for bad in bad_words)):
      continue

    # Reasonable lengths
    if not (10 < len(article_words) < 100 and
        3 < len(title_words) < 50):
      continue

    # Some word match.
    matches = len(set([w.lower() for w in title_words if len(w) > 3]) &
            set([w.lower() for w in article_words if len(w) > 3]))
    if matches < 1:
      continue

    t_f.write(title + "\n")
    a_f.write(article + "\n")
