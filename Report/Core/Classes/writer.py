__all__ = ['Writer']

from abc import abstractmethod, ABCMeta

from ..Classes import Container, WriteInfo
from ..Interface.interface import IWriter


class Writer(IWriter):
    __metaclass__ = ABCMeta

    def __init__(self, write_info):
        """
        Args:
            write_info (WriteInfo):
        """
        self._write_info = write_info

    def write(self, row, col, container):
        """
        Args:
            row (int):
            col (int):
            container (Container):
        """
        self._validate_container(container)
        for (row, col), cell in container.get_grid(row, col):
            cell.write(row, col, self._write_info)

    @abstractmethod
    def _validate_container(self, container):
        """
        Args:
            container (Container):
        """
        pass
