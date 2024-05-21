__all__ = ['Writer']

from ..Core.Classes import Writer as CoreWriter

from write_info import WriteInfo


class Writer(CoreWriter):

    def __init__(self, write_info):
        """
        Args:
            write_info (WriteInfo):
        """
        self._write_info = write_info

    def _validate_container(self, container):
        pass
