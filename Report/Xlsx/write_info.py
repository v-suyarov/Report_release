__all__ = ['WriteInfo']

from xlsxwriter.worksheet import Worksheet

from ..Core.Classes import WriteInfo as CoreWriteInfo


class WriteInfo(CoreWriteInfo):
    def __init__(self, worksheet):
        """
        Args:
            worksheet(Worksheet)
        """
        self.worksheet = worksheet

