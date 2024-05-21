__all__ = ['Column']

from abc import ABCMeta

from ..Interface.interface import ISizeable
from container import Container
from size import Size


class Column(Container):
    __metaclass__ = ABCMeta

    def __init__(self, *args):
        """
        Args:
            *args (ISizeable):
        """
        super(Column, self).__init__(*args)

    def _determine_size(self):
        """
        Returns:
             Size:
        """
        width, height = 0, 0
        for element in self._elements:
            element_size = element.get_size()
            height += element_size.height
            width = max(width, element_size.width)

        return Size(width, height)

    def _move_to_offset(self, row, col, element):
        """
        Args:
            row (int):
            col (int):
            element (ISizeable):
        Returns:
            tuple[int, int]:
        """
        row += element.get_size().height
        return row, col
