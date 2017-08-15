import argparse
from input import input_parser
from output import print_output
from solution import solve
from heuristics import HEURISTICS

parser = argparse.ArgumentParser()
parser.add_argument('PATTERN', nargs='?', default='', help='path to input pattern, if missing then reads from stdin')
parser.add_argument('--heuristic', default='mixed', choices=list(HEURISTICS.keys()))
parser.add_argument('--stats-only', action='store_true', default=False)
args = parser.parse_args()

pattern = input_parser(args.PATTERN)

ans = solve(pattern, heuristic=args.heuristic)
print_output(ans, stats_only=args.stats_only)

# academy172761