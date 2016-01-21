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
