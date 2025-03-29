'''
Created on 6 nov 2024

@author: Agustin
'''

from __future__ import annotations
from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar

E = TypeVar('E')

class Cola(AgregadoLineal[E]):
    @classmethod
    def of(cls) -> Cola[E]:
        return cls()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __str__(self):
        return f"Cola({self._elements})"

if __name__ == '__main__':
    pass