import sys
import os
from utils import print_error

def input_parser(filename):
    if filename and not os.path.exists(filename):
        print_error('{} does not exists')

    if filename:
        with open(filename) as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    lines = list(filter(bool, map(lambda s: s.split('#')[0].strip(), lines)))
    pattern = list(map(lambda x: list(map(int, x.split())), lines[1:]))

    return pattern