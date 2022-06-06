import yaml
from flatten_dict import flatten
import sys
import logging
from datetime import datetime

def Add(a, b):
    return a+b

if __name__ == '__main__':
    with open(sys.argv[1], encoding="utf8") as f:
        res = yaml.safe_load(f)
        kv = flatten(res, reducer='dot')
        print(kv)
        logging.warning(f' [{sys.argv[0]}@{datetime.now().isoformat()}] ' +
            f"2+3 = {Add(2,3)}")

