'''
Created on 6 nov 2024

@author: Agustin
'''

from __future__ import annotations

from typing import List, Generic, TypeVar, Callable
from abc import ABC, abstractmethod

E = TypeVar('E')

class AgregadoLineal(ABC, Generic[E]):
        
    def __init__(self):
        self._elements = []
        
    def size(self) -> int:
        return len(self._elements)
    
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    def elements(self) -> list[E]:
        return self._elements
    
    def add(self, e: E) -> None:
        pass
    
    def add_all(self, ls: List[E]) -> None:
        for element in ls:
            self.add(element)
            
    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)
    
    def remove_all(self) -> List[E]:
        removed = self._elements.copy()
        self._elements.clear()
        return removed
    
    # Ejercicio 2: MODIFICACIONES AÑADIDAS PARA LA DEFENSA 2
    
    def contains(self, e: E) -> bool:
        return e in self._elements
    
    def find(self, func: Callable[[E], bool]) -> E | None:
        for element in self._elements:
            if func(element):
                return element
        return None
    
    def filter(self, func: Callable[[E], bool]) -> list[E]:
        return [element for element in self._elements if func(element)]
    



if __name__ == '__main__':
    pass