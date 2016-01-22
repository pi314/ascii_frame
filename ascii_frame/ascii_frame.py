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


def wrap(data, width=0, padding=0, corners=".''.", edges='-|-|'):
    if width and padding:
        width -= 2 * padding
        if width <= 0:
            raise ValueError('No remain width available, increase width or decrease padding.')

    if len(corners) != 4:
        raise ValueError('Corners should be 4 characters/strings')

    corner_tr = corners[0]
    corner_br = corners[1]
    corner_bl = corners[2]
    corner_tl = corners[3]

    if len(edges) != 4:
        raise ValueError('Edges should be 4 characters/strings')

    edge_t = edges[0]
    edge_r = edges[1]
    edge_b = edges[2]
    edge_l = edges[3]

    ret = list(text_generator(data, width=width))
    max_len = max(*chain(ret).map(lambda lo: lo.width), width)

    return [
        '{ctl}{et}{ctr}'.format(
            ctl=corner_tl,
            et=edge_t * (max_len + 2 * padding),
            ctr=corner_tr,
        )] + chain(ret).map(
            lambda lo: '{el}{p}{t}{s}{p}{er}'.format(
                el=edge_l,
                t=lo.text, p=' ' * padding,
                s=' ' * (max_len - lo.width),
                er=edge_r,
            )
        ).list + ["{cbl}{eb}{cbr}".format(
            cbl=corner_bl,
            eb=edge_b * (max_len + 2 * padding),
            cbr=corner_br,
        )
    ]


def print(data, width=0, padding=0, corners=".''.", edges='-|-|', **kwargs):
    for l in wrap(data, width=width, padding=padding, corners=corners, edges=edges):
        print_(l, **kwargs)


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

    parser.add_argument('-c', '--corners',
        type=str,
        default=".''.",
        help='Customize corners of frame.  4 chars in clockwise order from top right.')

    parser.add_argument('-e', '--edges',
        type=str,
        default="-|-|",
        help='Customize corners of frame.  4 chars in clockwise order from top.')

    args = parser.parse_args()
    print(args.input_file,
        width=args.width,
        padding=args.padding,
        corners=args.corners,
        edges=args.edges)
