import json
import gzip

def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield json.dumps(eval(l))

f = open("meta_Clothing_Shoes_and_Jewelry.json", 'w')
for l in parse("meta_Clothing_Shoes_and_Jewelry.json.gz"):
  f.write(l + '\n')