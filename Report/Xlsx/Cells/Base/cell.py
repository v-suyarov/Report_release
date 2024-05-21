__all__ = [
    'Cell',
    'MergedStrategy',
    'UnMerged',
    'Merged'
]

from abc import ABCMeta, abstractmethod

from xlsxwriter.format import Format
from xlsxwriter.worksheet import Worksheet

from Report.Core.Classes import Cell as CoreCell, Size

from Report.Xlsx.write_info import WriteInfo


# TODO: try to move the MergedStrategy code into a separate module,
#  there were problems with cyclic import, because for typing you need to import Cell,
#  and Cell in turn requires import of MergedStrategy
class MergedStrategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def write(self, row, col, write_info, cell):
        """
        Args:
            row (int):
            col (int):
            write_info (WriteInfo):
            cell (Cell):
        """
        pass

    @property
    @abstractmethod
    def size(self):
        """
        Returns:
            Size:
        """
        pass


class Merged(MergedStrategy):

    def __init__(self, width, height):
        """
        Args:
            width (int):
            height (int):
        """
        self._size = Size(width, height)

    @property
    def size(self):
        return self._size

    def write(self, row, col, write_info, cell):
        """
        Args:
            row (int):
            col (int):
            write_info (WriteInfo):
            cell (Cell):
        """
        merged_size = self._size - Size.one()
        last_row = row + merged_size.height
        last_col = col + merged_size.width
        write_info.worksheet.merge_range(
            row, col, last_row, last_col, cell, cell.get_format())


class UnMerged(MergedStrategy):

    def __init__(self):
        self._size = Size.one()

    @property
    def size(self):
        return self._size

    def write(self, row, col, write_info, cell):
        """
        Args:
            row (int):
            col (int):
            write_info (WriteInfo):
            cell (Cell):
        """
        write_info.worksheet.write(row, col, cell, cell.get_format())


class Cell(CoreCell):
    __metaclass__ = ABCMeta

    def __init__(self, merged_strategy=UnMerged(), cell_format=None):
        """
        Args:
            merged_strategy (MergedStrategy):
            cell_format (Format):
        """
        self._merged_strategy = merged_strategy
        self._format = cell_format

    def get_format(self):
        """
        Returns:
             Format:
        """
        return self._format

    def get_size(self):
        """
        Returns:
            Size:
        """
        return self._merged_strategy.size

    def write(self, row, col, write_info):
        """
        Args:
            row (int):
            col (int):
            write_info (WriteInfo):
        """
        write_info.worksheet.add_write_handler(type(self), self._write_handler)
        self._merged_strategy.write(row, col, write_info, self)

    @staticmethod
    @abstractmethod
    def _write_handler(worksheet, row, col, cell, cell_format=None):
        """
        Args:
            worksheet (Worksheet):
            row (int):
            col (int):
            cell (TextCell):
            cell_format (Format):
        Returns:
            int:
        """
        pass
