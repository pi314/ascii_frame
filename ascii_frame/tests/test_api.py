import pytest

from ..ascii_frame import wrap


def test_basic():
    assert wrap(['ascii_frame']) == [
        '.-----------.',
        '|ascii_frame|',
        "'-----------'",
    ]


def test_multi_lines():
    assert wrap(['ascii_frame', 'test']) == [
        '.-----------.',
        '|ascii_frame|',
        '|test       |',
        "'-----------'",
    ]


def test_width_narrow():
    assert wrap(['ascii_frame'], width=3) == [
        '.---.',
        '|asc|',
        '|ii_|',
        '|fra|',
        '|me |',
        "'---'",
    ]

    assert wrap(['ascii', 'frame'], width=3) == [
        '.---.',
        '|asc|',
        '|ii |',
        '|fra|',
        '|me |',
        "'---'",
    ]


def test_width_wide():
    assert wrap(['a', 'b'], width=5) == [
        '.-----.',
        '|a    |',
        '|b    |',
        "'-----'",
    ]


def test_padding_basic():
    assert wrap(['ascii', 'frame'], padding=3) == [
        '.-----------.',
        '|   ascii   |',
        '|   frame   |',
        "'-----------'",
    ]


def test_narrow_width_with_padding():
    assert wrap(['ascii_frame'], width=9, padding=3) == [
        '.---------.',
        '|   asc   |',
        '|   ii_   |',
        '|   fra   |',
        '|   me    |',
        "'---------'",
    ]

    assert wrap(['ascii', 'frame'], width=9, padding=3) == [
        '.---------.',
        '|   asc   |',
        '|   ii    |',
        '|   fra   |',
        '|   me    |',
        "'---------'",
    ]


def test_wide_width_with_padding():
    assert wrap(['a', 'b'], width=15, padding=3) == [
        '.---------------.',
        '|   a           |',
        '|   b           |',
        "'---------------'",
    ]


def test_corners_basic():
    assert wrap(['YATTA'], corners='+') == [
        '+-----+',
        '|YATTA|',
        '+-----+',
    ]

    assert wrap(['YATTA'], corners='+#') == [
        '+-----+',
        '|YATTA|',
        '#-----#',
    ]

    assert wrap(['YATTA'], corners='+#$%') == [
        '%-----+',
        '|YATTA|',
        '$-----#',
    ]


def test_edges_basic():
    assert wrap(['YATTA'], corners='#', edges='#') == [
        '#######',
        '#YATTA#',
        '#######',
    ]

    assert wrap(['YATTA'], corners='/\\/\\', edges='|-') == [
        '\|||||/',
        '-YATTA-',
        '/|||||\\',
    ]

    assert wrap(['YATTA'], corners='#', edges='*|*') == [
        '#*****#',
        '|YATTA|',
        '#*****#',
    ]

    assert wrap(['YATTA'], corners=' ', edges='^>v<') == [
        ' ^^^^^ ',
        '<YATTA>',
        ' vvvvv ',
    ]


def test_corners_and_edges():
    assert wrap(['YATTA'], padding=1, corners=['++'], edges=['=', '||'] * 2) == [
        '++=======++',
        '|| YATTA ||',
        '++=======++',
    ]


def test_fancy_edges():
    assert wrap(['YATTA YATTA'], padding=1, corners='.*', edges=['-*-.', '|', "-.-*"]) == [
        '.-*-.-*-.-*-.-.',
        '| YATTA YATTA |',
        '*-.-*-.-*-.-*-*',
    ]

    assert wrap(['YATTA YATTA YATTA!!!!'], padding=1,
            corners='  _`',
            edges=['"*-=+._`', ')', '.+=-*"`_', '>']) == [
        '`"*-=+._`"*-=+._`"*-=+._ ',
        '> YATTA YATTA YATTA!!!! )',
        '_.+=-*"`_.+=-*"`_.+=-*"` ',
    ]

    # wide edges
    assert wrap(['YATTA'], corners='十' * 4, edges='十' * 4) == [
        '十十十十十',
        '十YATTA 十',
        '十十十十十',
    ]


def test_exceptions_narrow():
    # too narrow
    with pytest.raises(ValueError):
        wrap(['a'], width=3, padding=3)


def test_exceptions_make_up_corners():
    # automatically make up corners
    wrap(['a'], corners='.')
    wrap(['a'], corners=['.'])
    wrap(['a'], corners='.' * 2)
    wrap(['a'], corners=['.'] * 2)

    # not enough corner
    with pytest.raises(ValueError):
        wrap(['a'], corners='.' * 3)
        wrap(['a'], corners=['.'] * 3)

    # right corners amount
    wrap(['a'], corners='.' * 4)
    wrap(['a'], corners=['.'] * 4)

    # too many corners
    with pytest.raises(ValueError):
        wrap(['a'], corners='.' * 5)
        wrap(['a'], corners=['.'] * 5)


def test_exceptions_make_up_edges():
    # automatically make up edges
    wrap(['a'], edges='.')
    wrap(['a'], edges=['.'])
    wrap(['a'], edges='.' * 2)
    wrap(['a'], edges=['.'] * 2)
    wrap(['a'], edges='.' * 3)
    wrap(['a'], edges=['.'] * 3)

    # right edges amount
    wrap(['a'], edges='.' * 4)
    wrap(['a'], edges=['.'] * 4)

    # too many edges
    with pytest.raises(ValueError):
        wrap(['a'], edges='.' * 5)
        wrap(['a'], edges=['.'] * 5)

    # wide corners
    with pytest.raises(ValueError):
        wrap(['a'], corners=['++'] * 4, edges=['-', '|'] * 2)

    # wide edges
    with pytest.raises(ValueError):
        wrap(['a'], corners=['+'] * 4, edges=['-', '||'] * 2)

def test_exceptions_wide_corner_and_edges():
    # wide corners with wide edges, ok
    wrap(['a'], corners=['++'] * 4, edges=['-', '||'] * 2)
