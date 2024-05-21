__all__ = [
    'Text',
]

from xlsxwriter.format import Format
from xlsxwriter.worksheet import Worksheet

from Report.Xlsx.Cells.Base import ValueCell, MergedStrategy, UnMerged


class Text(ValueCell):
    def __init__(self, value, merged_strategy=UnMerged(), cell_format=None):
        """
        Args:
            value (unicode):
            merged_strategy (MergedStrategy):
            cell_format (Format):
        """
        super(Text, self).__init__(value, merged_strategy, cell_format)

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
                -2 String truncated to 32k characters.
        """
        return worksheet.write_string(
            row, col, cell.get_value(), cell_format)
