import sys
import re
import argparse

from .chain import chain
from .textobject import TextObject


print_ = print


def text_generator(data, width=None):
    m = chain(data).map(TextObject)

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

    if len(corners) == 1:
        corners = corners * 4

    if len(corners) == 2:
        corners = corners + corners[::-1]

    if len(corners) != 4:
        raise ValueError('Corners should be {1, 2, 4} characters/strings.')

    corner_tr = TextObject(corners[0], rstrip=False)
    corner_br = TextObject(corners[1], rstrip=False)
    corner_bl = TextObject(corners[2], rstrip=False)
    corner_tl = TextObject(corners[3], rstrip=False)

    if len(edges) == 1:
        edges = edges * 4

    elif len(edges) == 2:
        edges = edges * 2

    elif len(edges) == 3:
        edges = edges + edges[1]

    elif len(edges) != 4:
        raise ValueError('Edges should be 1 ~ 4 characters/strings')

    edge_t = TextObject(edges[0], rstrip=False)
    edge_r = TextObject(edges[1], rstrip=False)
    edge_b = TextObject(edges[2], rstrip=False)
    edge_l = TextObject(edges[3], rstrip=False)

    if not chain([edge_t, edge_b]).all(lambda e: e.width > 0):
        raise ValueError('Top and bottom edge\'s width should larger than 0.')

    if not chain([edge_r, corner_tr, corner_br]).map(lambda x: x.width).all_identical():
        raise ValueError('Corners and their neighbor edges should have same width.')

    if not chain([edge_l, corner_tl, corner_bl]).map(lambda x: x.width).all_identical():
        raise ValueError('Corners and their neighbor edges should have same width.')

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
