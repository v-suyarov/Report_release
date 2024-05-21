__all__ = [
    'Image',
]

from xlsxwriter.format import Format
from xlsxwriter.worksheet import Worksheet

from Report.Xlsx.write_info import WriteInfo
from Report.Xlsx.Cells.Base import Cell, UnMerged, MergedStrategy


class Image(Cell):

    def __init__(self, path, merged_strategy=UnMerged(), cell_format=None, options=None):
        """
        Args:
            path (unicode):
            merged_strategy (MergedStrategy):
            cell_format (Format):
        """
        super(Image, self).__init__(merged_strategy, cell_format)
        self._path = path
        self._options = options

    def get_path(self):
        """
        Returns:
            unicode:
        """
        return self._path

    def get_options(self):
        """
        Returns:
            dict:
        """
        return self._options

    def write(self, row, col, write_info):
        """
        Args:
            row (int):
            col (int):
            write_info (WriteInfo):
        """
        super(Image, self).write(row, col, write_info)
        write_info.worksheet.insert_image(
            row, col, self.get_path(), self.get_options())

    @staticmethod
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
                0  Success.
                -1 Row or column is out of worksheet bounds.
        """
        return worksheet.write_blank(
            row, col, None, cell_format)
