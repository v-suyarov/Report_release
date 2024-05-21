__all__ = ['WriteInfo']

from abc import ABCMeta

from ..Interface.interface import IWriteInfo


class WriteInfo(IWriteInfo):
    __metaclass__ = ABCMeta
