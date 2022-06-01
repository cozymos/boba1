import yaml
from flatten_dict import flatten
import sys

def Add(a, b):
    return a+b

if __name__ == '__main__':
    with open(sys.argv[1], encoding="utf8") as f:
        res = yaml.safe_load(f)
        kv = flatten(res, reducer='dot')
        print(Add(1,2), kv)
