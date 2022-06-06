from build2 import Add
import sys
import logging
from datetime import datetime

def TestAdd():
    assert Add(2,3) == 5
    print("assert test2")

if __name__ == '__main__':
    TestAdd()
    logging.warning(f' [{sys.argv[0]}@{datetime.now().isoformat()}] ' +
            '"passed"')
