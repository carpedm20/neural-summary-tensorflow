#-*- coding: utf-8 -*-
#!/bin/python
import re
import os
import sys
import json
from collections import defaultdict

input_path = sys.argv[1]
try:
  is_korean = sys.argv[2]
except:
  is_korean = False

title_path = os.path.join(os.path.dirname(input_path), "title.txt")
article_path = os.path.join(os.path.dirname(input_path), "article.txt")

def remove_digits(parse):
  return re.sub(ur"…", "", re.sub(ur".+ (기자|특파원) = ", "", re.sub(ur'(·|!|\'|`|"|‘|’|“|”|=|ㆍ)', " ", re.sub(r'\d+', '#', parse))))

case = defaultdict(int)

with open(input_path) as f, \
     open(title_path, "w") as t_f, \
     open(article_path, "w") as a_f:
  try:
    from tqdm import tqdm
    items = tqdm(json.loads(f.read()))
  except:
    items = json.loads(f.read())

  for item in items:
    title = " ".join(remove_digits(item['t']).lower().split())
    article = " ".join(remove_digits(item['a']).lower().split())

    title = re.sub(r'\[.+\]', '', title).strip()
    title = re.sub(r'\(.+\)', '', title).strip()
    article = re.sub(r'\[.+\]', '', article).strip()
    article = re.sub(r'\(.+\)', '', article).strip()

    if u'\ub2e4.' in article:
      article = article.split(u'\ub2e4.', 1)[0]
      article = article + u'\ub2e4'

    title_words = title.strip().split()
    article_words = article.strip().split()

    # No blanks.
    if any((word == "" for word in title_words)) or title_words == []:
      case['empty_title'] += 1
      continue

    if any((word == "" for word in article_words)) or article_words == []:
      case['empty_article'] += 1
      continue

    if is_korean:
      if article_words[-1][-1] != u"다":
        case['not_end_with_da'] += 1
        continue

        if article[-2:] != u'\ub2e4.':
          continue

      if len(re.findall(r"\w", article)) > 20 or len(re.findall(r"\w", title)) > 10:
        case['only english'] += 1
        continue

    bad_words = [u'?', u'＂', u"-"]

    if any((bad in title.lower()
        for bad in bad_words)):
      case['bad in title'] += 1
      continue

    bad_words = ['======', u'＂']

    if any((bad in article.lower()
        for bad in bad_words)):
      case['bad in article'] += 1
      continue

    # Reasonable lengths
    if not (10 < len(article_words) < 100 and
        2 < len(title_words) < 50):
      case['reasonable length'] += 1
      continue

    # Some word match.
    if is_korean:
      matches = len(set([w[:2] for w in title_words if len(w) > 1]) &
                    set([w[:2] for w in article_words if len(w) > 1]))
    else:
      matches = len(set([w for w in title_words if len(w) > 1]) &
                    set([w for w in article_words if len(w) > 1]))
    if matches < 1:
      case['zero match'] += 1
      continue

    t_f.write(title.encode('utf-8') + "\n")
    a_f.write(article.encode('utf-8') + "\n")

print case
