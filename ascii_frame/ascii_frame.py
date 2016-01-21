import sys
import re
import argparse

from .chain import chain
from unicodedata import east_asian_width as uwidth
# for more information, see http://unicode.org/reports/tr11/


print_ = print


def text_generator(data):
    return chain(data).map(
        str.rstrip
    ).map(
        lambda s: re.sub(r'\x1b\[[^hm]*[hm]', '', s)
    ).map(
        lambda s: (sum(1+(uwidth(c) in 'WF') for c in s), s)
    )


def wrap(data, width=None, padding=None):
    ret = text_generator(data).list

    max_len = max(ret, key=lambda t: t[0])[0]

    return ['.{}.'.format('-' * max_len)] + chain(ret).map(
        lambda s: '|{t}{s}|'.format(
            t=s[1],
            s=' ' * (max_len-s[0])
        )
    ).list + ["'{}'".format('-' * max_len)]


def print(args):
    for l in wrap(args.input_file, width=args.width, padding=args.padding):
        print_(l)


def main():
    parser = argparse.ArgumentParser(
        prog='ascii_frame',
        description='Wrap text with an ASCII frame.',
    )

    parser.add_argument('-w', '--width',
        type=int,
        help='Set the width of ASCII frame.')

    parser.add_argument('-p', '--padding',
        type=int,
        help='Set the padding of ASCII frame.')

    parser.add_argument('-f', '--input-file',
        type=argparse.FileType('r'),
        default=sys.stdin,
        help='Read content from file.')

    args = parser.parse_args()
    print(args)
