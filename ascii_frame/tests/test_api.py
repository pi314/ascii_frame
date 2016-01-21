from pytest import raises
from unittest.mock import patch, Mock

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

def test_width_constrain():
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
