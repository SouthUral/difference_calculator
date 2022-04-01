import argparse
import json
from general_code.diff_code import diff_files

parser = argparse.ArgumentParser()
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()


def main():
    first_file = json.load(open(args.first_file))
    second_file = json.load(open(args.second_file))
    print(diff_files.generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
