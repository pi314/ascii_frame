class chain:
    def __init__(self, value):
        self.value = value
        for attr in dir(value):
            if not attr.startswith('__'):
                self.__dict__[attr] = getattr(self.value, attr)

    def __iter__(self):
        for i in self.value:
            yield i

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, chain):
            return chain(self.value + other.value)
        return chain(self.value + other)

    def __sub__(self, other):
        if isinstance(other, chain):
            return chain(self.value - other.value)
        return chain(self.value - other)

    def map(self, func):
        return chain(map(func, self.value))

    def filter(self, func):
        return chain(filter(func, self.value))

    def all(self, func):
        return all(self.map(func))

    def all_identical(self):
        return len(set(self.value)) <= 1

    @property
    def list(self):
        return list(self)

    @property
    def dict(self):
        return dict(self)

    @property
    def set(self):
        return set(self)
