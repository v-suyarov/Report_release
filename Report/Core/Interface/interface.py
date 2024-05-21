__all__ = [
    'ISizeable',
    'IExtendable',
    'IWriter',
    'IWriteInfo',
    'IWritable'
]

from abc import ABCMeta, abstractmethod

from Report.Core.Classes import Size


class ISizeable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_size(self):
        """
        Returns:
            Size:
        """
        pass


class IWriteInfo(object):
    __metaclass__ = ABCMeta


class IWritable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def write(self, row, col, write_info):
        """
        Args:
            row (int):
            col (int):
            write_info (IWriteInfo):
        """
        pass


class IExtendable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def extend(self, elements):
        """
        Args:
            elements (Iterable[ISizeable]):
        """
        pass


class IWriter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def write(self, row, col, container):
        """
        Args:
            row (int):
            col (int):
            container (Container):
        """
        pass
