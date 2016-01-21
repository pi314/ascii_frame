import sys
import re
import argparse

from .chain import chain
from unicodedata import east_asian_width
# for more information, see http://unicode.org/reports/tr11/


print_ = print


def uwidth(c):
    return 1 + (east_asian_width(c) in 'WF')


def text_generator(data, width=None):
    m = chain(data).map(
        lambda s: re.sub(r'\x1b\[[^hm]*[hm]', '', s.rstrip())
    ).map(
        lambda s: (sum(uwidth(c) for c in s), s)
    )

    for pair in m:
        if width and width > 0 and pair[0] > width:
            for i in break_line(pair[1], width):
                yield i
        else:
            yield pair


def break_line(s, width):
    w, ret = 0, ''
    for c in s:
        if w + uwidth(c) > width:
            yield (w, ret)
            w, ret = 0, ''

        w, ret = w + uwidth(c), ret + c

    yield (w, ret)


def wrap(data, width=None, padding=None):
    ret = list(text_generator(data, width=width))

    max_len = max(ret, key=lambda t: t[0])[0]
    if isinstance(width, int):
        max_len = max(max_len, width)

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
