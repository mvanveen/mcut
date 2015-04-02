from operator import itemgetter


class ColorCube(object):
    _rmax = 255.
    _rmin = 0.
    _gmax = 255.
    _gmin = 0.
    _bmax = 255.
    _bmin = 0.

    def __init__(self, *colors):
        self._colors = colors or []
        self.resize()

    @property
    def colors(self):
        return self._colors

    @property
    def rsize(self):
        return self._rmax - self._rmin

    @property
    def gsize(self):
        return self._gmax - self._gmin

    @property
    def bsize(self):
        return self._bmax - self._bmin

    @property
    def size(self):
        return self.rsize, self.gsize, self.bsize

    def _average(self, col, length):
        return sum(col) / length

    def color_columns(self):
        return [
            [_[0] for _ in self.colors],
            [_[1] for _ in self.colors],
            [_[2] for _ in self.colors],
        ]

    @property
    def average(self):
        length = len(self.colors)
        cols = self.color_columns()
        r, g, b = [self._average(col, length) for col in cols]
        return r, g, b

    def resize(self):
        col_r, col_g, col_b = self.color_columns()

        self._rmin = min(col_r)
        self._rmax = max(col_r)
        self._gmin = min(col_g)
        self._gmax = max(col_g)
        self._bmin = min(col_b)
        self._bmax = max(col_b)

    def split(self, axis):
        self.resize()
        self._colors = sorted(self.colors, key=itemgetter(axis))

        # Find median
        med_idx = len(self.colors) / 2

        # Create splits
        return (
            ColorCube(*self.colors[:med_idx]),
            ColorCube(*self.colors[med_idx:]
        ))
