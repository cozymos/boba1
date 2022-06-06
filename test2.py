from main1 import Add
import logging

def TestAdd():
    assert Add(2,3) == 5
    print("Test passed")

if __name__ == '__main__':
    TestAdd()
    logging.warning("end of test1")
