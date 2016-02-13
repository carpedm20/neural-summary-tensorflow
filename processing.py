#-*- coding: utf-8 -*-
#!/bin/python
import re
import os
import sys
import json

input_path = sys.argv[1]
try:
  is_korean = sys.argv[2]
except:
  is_korean = False

title_path = os.path.join(os.path.dirname(input_path), "title.txt")
article_path = os.path.join(os.path.dirname(input_path), "article.txt")

def remove_digits(parse):
    return re.sub(ur".+ (기자|특파원) = ", "", re.sub('(`|"|‘|’)',"'", re.sub(r'\d', '#', parse)))

with open(input_path) as f, \
     open(title_path, "w") as t_f, \
     open(article_path, "w") as a_f:
  for item in json.loads(f.read()):
    title = remove_digits(" ".join(item['t'].split())).lower()
    article = remove_digits(" ".join(item['a'].split())).lower()

    title = re.sub(r'\[.+\]', '', title).strip()
    title = re.sub(r'\(.+\)', '', title).strip()
    article = re.sub(r'\[.+\]', '', article).strip()
    article = re.sub(r'\(.+\)', '', article).strip()

    title_words = title.strip().split()
    article_words = article.strip().split()

    # No blanks.
    if any((word == "" for word in title_words)) or title_words == []:
      continue

    if any((word == "" for word in article_words)) or article_words == []:
      continue

    if is_korean and article_words[-1][-1] != u"다":
      continue

    bad_words = ['?', ' : ', ' - ']

    if any((bad in title.lower()
        for bad in bad_words)):
      continue

    bad_words = ['======']

    if any((bad in article.lower()
        for bad in bad_words)):
      continue

    # Reasonable lengths
    if not (10 < len(article_words) < 100 and
        3 < len(title_words) < 50):
      continue

    # Some word match.
    matches = len(set([w for w in title_words if len(w) > 3]) &
            set([w for w in article_words if len(w) > 3]))
    if matches < 1:
      continue

    t_f.write(title.encode('utf-8') + "\n")
    a_f.write(article.encode('utf-8') + "\n")
