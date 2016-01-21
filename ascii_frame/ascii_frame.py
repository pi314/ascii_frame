import sys
import re
import argparse

from .chain import chain
from .lineobject import LineObject


print_ = print


def text_generator(data, width=None):
    m = chain(data).map(LineObject)

    for lo in m:
        if width and width > 0 and lo.width > width:
            for i in lo.wrap(width):
                yield i
        else:
            yield lo


def wrap(data, width=None, padding=None):
    ret = list(text_generator(data, width=width))

    max_len = max(ret, key=lambda lo: lo.width).width
    if isinstance(width, int):
        max_len = max(max_len, width)

    return ['.{}.'.format('-' * max_len)] + chain(ret).map(
        lambda lo: '|{t}{s}|'.format(
            t=lo.text,
            s=' ' * (max_len - lo.width)
        )
    ).list + ["'{}'".format('-' * max_len)]


def print(data, width=None, padding=None):
    for l in wrap(data, width=width, padding=padding):
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
    print(args.input_file, width=args.width, padding=args.padding)
