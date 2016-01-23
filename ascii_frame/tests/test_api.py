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


def test_width_narrow_with_padding():
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


def test_width_wide_with_padding():
    assert wrap(['a', 'b'], width=15, padding=3) == [
        '.---------------.',
        '|   a           |',
        '|   b           |',
        "'---------------'",
    ]


def test_corners_and_edges():
    assert wrap(['a', 'b'], width=15, padding=3, corners="A") == [
        'A---------------A',
        '|   a           |',
        '|   b           |',
        "A---------------A",
    ]

    assert wrap(['a', 'b'], width=15, padding=3, corners="AB") == [
        'A---------------A',
        '|   a           |',
        '|   b           |',
        "B---------------B",
    ]

    assert wrap(['a', 'b'], width=15, padding=3, edges="A") == [
        '.AAAAAAAAAAAAAAA.',
        'A   a           A',
        'A   b           A',
        "'AAAAAAAAAAAAAAA'",
    ]

    assert wrap(['a', 'b'], width=15, padding=3, edges="AB") == [
        '.AAAAAAAAAAAAAAA.',
        'B   a           B',
        'B   b           B',
        "'AAAAAAAAAAAAAAA'",
    ]

    assert wrap(['a', 'b'], width=15, padding=3, corners="ABCD", edges="EFG") == [
        'DEEEEEEEEEEEEEEEA',
        'F   a           F',
        'F   b           F',
        "CGGGGGGGGGGGGGGGB",
    ]

    assert wrap(['a', 'b'], width=15, padding=3, corners="ABCD", edges="EFGH") == [
        'DEEEEEEEEEEEEEEEA',
        'H   a           F',
        'H   b           F',
        "CGGGGGGGGGGGGGGGB",
    ]

    assert wrap(['a', 'b'], width=15, padding=3, corners=['++'], edges=['=', '||'] * 2) == [
        '++===============++',
        '||   a           ||',
        '||   b           ||',
        "++===============++",
    ]

    assert wrap(['a', 'b'], width=15, padding=3, corners=' ', edges='^>v<') == [
        ' ^^^^^^^^^^^^^^^ ',
        '<   a           >',
        '<   b           >',
        " vvvvvvvvvvvvvvv ",
    ]


def test_exceptions():
    # too narrow
    with pytest.raises(ValueError):
        wrap(['a'], width=3, padding=3)

    # automatically make up corners
    wrap(['a'], corners='.')
    wrap(['a'], corners='.' * 2)

    # not enough corner
    with pytest.raises(ValueError):
        wrap(['a'], corners='.' * 3)

    # right corners amount
    wrap(['a'], corners='.' * 4)

    # too many corners
    with pytest.raises(ValueError):
        wrap(['a'], corners='.' * 5)

    # automatically make up edges
    wrap(['a'], edges='.')
    wrap(['a'], edges='.' * 2)
    wrap(['a'], edges='.' * 3)

    # right edges amount
    wrap(['a'], edges='.' * 4)

    # too many edges
    with pytest.raises(ValueError):
        wrap(['a'], edges='.' * 5)

    # wide corners
    with pytest.raises(ValueError):
        wrap(['a'], corners=['++'] * 4, edges=['-', '|'] * 2)

    # wide edges
    with pytest.raises(ValueError):
        wrap(['a'], corners=['+'] * 4, edges=['-', '||'] * 2)

    # wide corners with wide edges, ok
    wrap(['a'], corners=['++'] * 4, edges=['-', '||'] * 2)
