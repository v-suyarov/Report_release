__all__ = ['Row']

from abc import ABCMeta

from ..Interface.interface import ISizeable
from container import Container
from size import Size


class Row(Container):
    __metaclass__ = ABCMeta

    def __init__(self, *args):
        """
        Args:
            *args (ISizeable):
        """
        super(Row, self).__init__(*args)

    def _determine_size(self):
        """
        Returns:
             Size:
        """
        width, height = 0, 0
        for element in self._elements:
            element_size = element.get_size()
            width += element_size.width
            height = max(height, element_size.height)

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
        col += element.get_size().width
        return row, col
