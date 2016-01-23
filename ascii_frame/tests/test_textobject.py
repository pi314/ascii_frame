from ..textobject import TextObject


def test_textobject_text():
    assert TextObject('normal').text == 'normal'
    assert TextObject('right  ').text == 'right'
    assert TextObject('\033[1;31mColor!\033[m   ').text == '\033[1;31mColor!\033[m'


def test_textobject_width():
    assert TextObject('normal').width == 6
    assert TextObject('中文').width == 4
    assert TextObject('\033[1;31mColor!\033[m   ').width == len('Color!')
    assert TextObject('\033[1;31m中文\033[m   ').width == TextObject('中文').width


def test_textobject_eq_str():
    assert TextObject('normal') == TextObject('normal')
    assert TextObject('normal') == 'normal'


def test_textobject_wrap():
    assert list(TextObject('normal text').wrap(100)) == ['normal text']
    assert list(TextObject('normal text').wrap(5)) == ['norma', 'l tex', 't']
    assert list(TextObject('中文').wrap(1)) == ['中', '文']
