__all__ = [
    'Number',
]


from xlsxwriter.format import Format
from xlsxwriter.worksheet import Worksheet

from Report.Xlsx.Cells.Base import ValueCell, MergedStrategy, UnMerged


class Number(ValueCell):
    def __init__(self, value, merged_strategy=UnMerged(), cell_format=None):
        """
        Args:
            value (int|float):
            merged_strategy (MergedStrategy):
            cell_format (Format):
        """
        super(Number, self).__init__(value, merged_strategy, cell_format)

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
        return worksheet.write_number(
            row, col, cell.get_value(), cell_format)
