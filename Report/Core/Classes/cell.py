__all__ = [
    'Cell',
]

from abc import ABCMeta

from ..Interface import ISizeable, IWritable
from ..Classes.size import Size


class Cell(ISizeable, IWritable):
    __metaclass__ = ABCMeta
