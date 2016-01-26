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
        edges = edges + edges[1:2]

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
    max_width = max(*chain(ret).map(lambda lo: lo.width), width)
    edge_t = edge_t.repeat_to(max_width + 2 * padding)
    edge_b = edge_b.repeat_to(max_width + 2 * padding)
    max_width = max(max_width, edge_t.width - 2 * padding, edge_b.width - 2 * padding)

    return [
        '{ctl}{et}{ctr}'.format(
            ctl=corner_tl,
            et=edge_t,
            ctr=corner_tr,
        )] + chain(ret).map(
            lambda lo: '{el}{p}{t}{s}{p}{er}'.format(
                el=edge_l,
                p=' ' * padding,
                t=lo.text,
                s=' ' * (max_width - lo.width),
                er=edge_r,
            )
        ).list + ["{cbl}{eb}{cbr}".format(
            cbl=corner_bl,
            eb=edge_b,
            cbr=corner_br,
        )
    ]


def print(data, width=0, padding=0, corners=".''.", edges='-|-|', **kwargs):
    for l in wrap(data, width=width, padding=padding, corners=corners, edges=edges):
        print_(l, **kwargs)


def frame_argument(v):
    ret = v

    if len(ret) == 1:
        ret = ret * 4

    if len(ret) == 2:
        ret = ret + ret[::-1]

    if len(ret) != 4:
        raise argparse.ArgumentTypeError('Corners should be {1, 2, 4} characters/strings.')

    return ret



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
        type=str, nargs='*', default=".''.",
        help='Customize corners of frame.  4 chars in clockwise order from top right.')

    parser.add_argument('-e', '--edges',
        type=str, nargs='*', default="-|-|",
        help='Customize corners of frame.  4 chars in clockwise order from top.')

    args = parser.parse_args()
    print(args.input_file,
        width=args.width,
        padding=args.padding,
        corners=args.corners,
        edges=args.edges)
