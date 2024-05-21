__all__ = ['Row']

from ..Core.Classes import Row as CoreRow
from ..Core.Interface import ISizeable


class Row(CoreRow):

    def __init__(self, *args):
        """
        Args:
            *args (ISizeable):
        """
        super(Row, self).__init__(*args)

    def _validate_element(self, element):
        """
        Args:
            element (ISizeable):
        """
        pass
