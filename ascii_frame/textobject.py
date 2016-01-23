import re
import math

from unicodedata import east_asian_width
# for more information, see http://unicode.org/reports/tr11/


class TextObject:
    @classmethod
    def uwidth(cls, c):
        return 1 + (east_asian_width(c) in 'WF')

    def __init__(self, text):
        self.text = text.rstrip()

    @property
    def width(self):
        return sum(
                1 + (east_asian_width(c) in 'WF')
                for c in re.sub(r'\x1b\[[^hm]*[hm]', '', self.text))

    def wrap(self, width):
        w, ret = 0, ''
        for c in self.text:
            if w + self.uwidth(c) > width and w > 0:
                yield TextObject(ret)
                w, ret = 0, ''

            w, ret = w + self.uwidth(c), ret + c

        yield TextObject(ret)

    def __str__(self):
        return self.text

    def __eq__(self, other):
        if isinstance(other, str):
            return self.text == other

        if isinstance(other, TextObject):
            return self.text == other.text

        return str(self) == str(other)

    def __mul__(self, multiplier):
        return self.text * multiplier

    def repeat_to(self, goal_width):
        return TextObject(self.text * math.ceil(goal_width / self.width))
