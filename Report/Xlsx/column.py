__all__ = ['Column']

from ..Core.Classes import Column as CoreColumn
from ..Core.Interface import ISizeable


class Column(CoreColumn):

    def __init__(self, *args):
        """
        Args:
            *args (ISizeable):
        """
        super(Column, self).__init__(*args)

    def _validate_element(self, element):
        """
        Args:
            element (ISizeable):
        """
        pass
