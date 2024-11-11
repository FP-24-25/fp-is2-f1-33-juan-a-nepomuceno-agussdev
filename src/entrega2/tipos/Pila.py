'''
Created on 6 nov 2024

@author: Agustin
'''

from __future__ import annotations
from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar

E = TypeVar('E')

class Pila(AgregadoLineal[E]):
    @classmethod
    def of(cls) -> Pila[E]:
        return cls()

    def add(self, e: E) -> None:
        self._elements.insert(0, e)

    def __str__(self):
        return f"Pila({self._elements})"
    
if __name__ == '__main__':
    pass