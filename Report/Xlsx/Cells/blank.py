__all__ = [
    'Blank',
]

from xlsxwriter.format import Format
from xlsxwriter.worksheet import Worksheet

from Report.Xlsx.Cells.Base import ValueCell, MergedStrategy, UnMerged


class Blank(ValueCell):
    def __init__(self, merged_strategy=UnMerged(), cell_format=None):
        """
        Args:
            merged_strategy (MergedStrategy):
            cell_format (Format):
        """
        super(Blank, self).__init__(None, merged_strategy, cell_format)

    @staticmethod
    def _write_handler(worksheet, row, col, cell, cell_format=None):
        """
        Args:
            worksheet (Worksheet):
            row (int):
            col (int):
            cell (ValueCell):
            cell_format (Format):
        Returns:
            int:
                0  Success.
                -1 Row or column is out of worksheet bounds.
        """
        return worksheet.write_blank(
            row, col, cell.get_value(), cell_format)
