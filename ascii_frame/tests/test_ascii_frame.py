from pytest import raises
from unittest.mock import patch, Mock

from ..ascii_frame import (wrap, break_line)


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

def test_width_constrain():
    assert list(break_line('ascii_frame', 3)) == [
        (3, 'asc'),
        (3, 'ii_'),
        (3, 'fra'),
        (2, 'me'),
    ]

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

def test_width_wider():
    assert wrap(['a', 'b'], width=5) == [
        '.-----.',
        '|a    |',
        '|b    |',
        "'-----'",
    ]
