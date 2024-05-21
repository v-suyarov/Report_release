__all__ = [
    'Container',
    'ExtendableContainer'
]

from abc import abstractmethod, ABCMeta
from collections import Iterable

from ..Interface.interface import ISizeable, IExtendable
from ..Classes import Cell
from size import Size


class Container(ISizeable):
    __metaclass__ = ABCMeta

    def __init__(self, *args):
        """
        Args:
            *args (ISizeable):
        """
        self._elements = self._init_elements(args)
        self._size = self._determine_size()
        self._grid = self._determine_grid()

    def get_grid(self, row=0, col=0):
        """
        Args:
            row (int):
            col (int):
        Returns:
            list[tuple[tuple[int, int], ISizeable]]:
        """
        if not row and not col:
            return self._grid

        grid = []
        for (local_row, local_col), cell in self._grid:
            global_row = local_row + row
            global_col = local_col + col
            grid.append(((global_row, global_col), cell))

        return grid

    def get_size(self):
        """
        Returns:
            Size:
        """
        return self._size

    def _init_elements(self, elements):
        """
        Args:
            elements (Iterable[ISizeable]):
        Returns:
            list[ISizeable]:
        """
        self._validate_elements(elements)
        return list(elements)

    def _validate_elements(self, elements):
        """
        Args:
            elements (Iterable[ISizeable]):
        """
        for element in elements:
            self._validate_element(element)

    def _determine_grid(self, row=0, col=0):
        """
        Args:
            row (int):
            col (int):
        Returns:
            list[tuple[tuple[int, int], Cell]]:
        """
        pos_and_cells = []
        for element in self._elements:
            if isinstance(element, Container):
                pos_and_cells.extend(
                    element.get_grid(row, col))
            else:
                pos_and_cells.append(((row, col), element))
            row, col = self._move_to_offset(row, col, element)

        return pos_and_cells

    @abstractmethod
    def _validate_element(self, element):
        """
        Args:
            element (ISizeable):
        """
        pass

    @abstractmethod
    def _determine_size(self):
        """
        Returns:
             Size:
        """
        pass

    @abstractmethod
    def _move_to_offset(self, row, col, element):
        """
        Args:
            row (int):
            col (int):
            element (ISizeable):
        Returns:
            tuple[int, int]:
        """
        pass


class ExtendableContainer(Container, IExtendable):
    # TODO: class has not been used anywhere yet
    __metaclass__ = ABCMeta

    def __init__(self, *args):
        """
        Args:
            *args (ISizeable):
        """
        super(ExtendableContainer, self).__init__(*args)

    def extend(self, elements):
        """
        Args:
            elements (Iterable[ISizeable]):
        """
        self._validate_elements(elements)
        self._elements.extend(elements)
        self._determine_size()
        self._determine_grid()
