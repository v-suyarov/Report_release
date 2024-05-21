__all__ = ['Size']


class Size(object):

    def __init__(self, width, height):
        """
        Args:
            width (int):
            height (int):
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @staticmethod
    def one():
        return Size(1, 1)

    @staticmethod
    def zero():
        return Size(0, 0)

    def __add__(self, other):
        """
        Args:
            other (Size):
        """
        return Size(self.width + other.width, self.height + other.height)

    def __eq__(self, other):
        """
        Args:
            other (Size):
        """
        if self.width == other.width and self.height == other.height:
            return True
        return False

    def __sub__(self, other):
        """
        Args:
            other (Size):
        """
        return Size(self.width - other.width, self.height - other.height)
