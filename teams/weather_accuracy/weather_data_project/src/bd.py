import Driver
import argparse
from collections import defaultdict

debug = False

def parseArguments():
    parser = argparse.ArgumentParser(usage='%(prog)s [options]',
                                     description='bd application')

    parser.add_argument('--debug', action='store_true', default=False)

    parser.add_argument('-p', '--path', dest='path', default=2.0,
                        help='set path to config.txt file')

    return parser.parse_args()

if __name__ == "__main__":
    config = defaultdict(list)
    args = parseArguments()
    driver = Driver.Driver().run('../config.txt')
    debug = args.debug
