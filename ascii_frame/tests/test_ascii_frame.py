from pytest import raises
from unittest.mock import patch, Mock

from ..ascii_frame import wrap

def test_normal():
    assert wrap(['ascii_frame']) == [
        '.-----------.',
        '|ascii_frame|',
        "'-----------'"
    ]

