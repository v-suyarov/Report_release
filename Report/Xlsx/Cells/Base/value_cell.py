__all__ = [
    'ValueCell',
]

from abc import ABCMeta, abstractmethod

from xlsxwriter.format import Format
from xlsxwriter.worksheet import Worksheet

from Report.Xlsx.Cells.Base import Cell, MergedStrategy, UnMerged


class ValueCell(Cell):
    __metaclass__ = ABCMeta

    def __init__(self, value, merged_strategy=UnMerged(), cell_format=None):
        """
        Args:
            value (Any):
            merged_strategy (MergedStrategy):
            cell_format (Format):
        """
        super(ValueCell, self).__init__(merged_strategy, cell_format)
        self._value = value

    def get_value(self):
        """
        Returns:
            Any:
        """
        return self._value

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
