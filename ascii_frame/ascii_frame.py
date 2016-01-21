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


def wrap(data, width=0, padding=0):
    if width and padding:
        width -= 2 * padding
        if width <= 0:
            raise ValueError('No remain width available, increase width or decrease padding.')

    ret = list(text_generator(data, width=width))

    max_len = max(*chain(ret).map(lambda lo: lo.width), width)

    return ['.{}.'.format('-' * (max_len + 2 * padding))] + chain(ret).map(
        lambda lo: '|{p}{t}{s}{p}|'.format(
            t=lo.text, p=' ' * padding,
            s=' ' * (max_len - lo.width)
        )
    ).list + ["'{}'".format('-' * (max_len + 2 * padding))]


def print(data, width=0, padding=0):
    for l in wrap(data, width=width, padding=padding):
        print_(l)


def main():
    parser = argparse.ArgumentParser(
        prog='ascii_frame',
        description='Wrap text with an ASCII frame.',
    )

    parser.add_argument('-w', '--width',
        type=int, default=0,
        help='Set the width of ASCII frame.')

    parser.add_argument('-p', '--padding',
        type=int, default=0,
        help='Set the padding of ASCII frame.')

    parser.add_argument('-f', '--input-file',
        type=argparse.FileType('r'),
        default=sys.stdin,
        help='Read content from file.')

    args = parser.parse_args()
    print(args.input_file, width=args.width, padding=args.padding)
