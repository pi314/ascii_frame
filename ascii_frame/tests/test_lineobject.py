from pytest import raises
from unittest.mock import patch, Mock

from ..lineobject import LineObject


def test_lineobject_text():
    assert LineObject('normal').text == 'normal'
    assert LineObject('right  ').text == 'right'
    assert LineObject('\033[1;31mColor!\033[m   ').text == 'Color!'


def test_lineobject_width():
    assert LineObject('normal').width == 6
    assert LineObject('中文').width == 4


def test_lineobject_eq_str():
    assert LineObject('normal') == LineObject('normal')
    assert LineObject('normal') == 'normal'


def test_lineobject_wrap():
    assert list(LineObject('normal text').wrap(100)) == ['normal text']
    assert list(LineObject('normal text').wrap(5)) == ['norma', 'l tex', 't']
    assert list(LineObject('中文').wrap(1)) == ['中', '文']
