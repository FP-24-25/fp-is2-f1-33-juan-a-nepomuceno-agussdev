'''
Created on 21 nov 2024

@author: Agustin
'''

# Ejercicio 1: Implementación de la cola con límite

from __future__ import annotations
from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar

E = TypeVar('E')

class ColaConLimite(AgregadoLineal[E]):
    def __init__(self, capacidad: int):
        # Constructor que inicia la cola con una capacidad máxima
        super().__init__()
        assert capacidad > 0, "La capacidad debe ser mayor que 0"
        self.__capacidad = capacidad
    
    @classmethod
    def of(cls, capacidad: int) -> ColaConLimite[E]:
        # Crea una nueva instancia con una capacidad máxima
        assert capacidad > 0, "La capacidad debe ser mayor que 0"
        return cls(capacidad)
    
    def is_full(self) -> bool:
        # Comprueba si la cola ha alcanzado su capacidad máxima
        return len(self._elements) >= self.__capacidad
    
    def add(self, e: E) -> None:
        # Añade un elemento a la cola si hay espacio
        # Lanza OverflowError si la cola está llena
        if self.is_full():
            raise OverflowError("La cola está llena")
        self._elements.append(e)

# Ejercicio 3: Funciones para hacer testing de las modificaciones realizadas

def test_cola_limite_completo():
    print("\n=== Tests ColaConLimite ===")
    cola = ColaConLimite.of(3)
    
    print("Añadiendo tareas...")
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")

    try:
        print("Intentando añadir cuando la cola está llena...")
        cola.add("Tarea 4")
    except OverflowError as e:
        print(f"Error: {e}")
    
    print(f"Eliminando: {cola.remove()}")

def test_contains():
    print("\n=== Tests contains ===")
    cola = ColaConLimite.of(5)
    
    # Test con cola vacía
    print(f"¿Contiene 'Tarea 1' en cola vacía?: {cola.contains('Tarea 1')}")
    
    # Test con elementos
    print("Añadimos Tarea 1 y Tarea 2 para probar...")
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    print(f"¿Contiene 'Tarea 1'?: {cola.contains('Tarea 1')}")
    print(f"¿Contiene 'Tarea 3'?: {cola.contains('Tarea 3')}")

def test_find():
    print("\n=== Tests find ===")
    cola = ColaConLimite.of(5)
    
    # Test con cola vacía
    print(f"Buscar en cola vacía: {cola.find(lambda x: len(x) > 5)}")
    
    # Añadir elementos para pruebas
    cola.add("Tarea corta")
    cola.add("Tarea mediana")
    cola.add("Tarea muy larga")
    
    # Test encontrar primer elemento que cumple condición
    print(f"Encontrar tarea con longitud > 10: {cola.find(lambda x: len(x) > 10)}")
    
    # Test cuando no hay coincidencias
    print(f"Encontrar tarea con longitud < 5: {cola.find(lambda x: len(x) < 5)}")

def test_filter():
    print("\n=== Tests filter ===")
    cola = ColaConLimite.of(5)
    
    # Test con cola vacía
    print(f"Filtrar cola vacía: {cola.filter(lambda x: len(x) > 5)}")
    
    # Añadir elementos variados
    cola.add("Tarea 1")
    cola.add("Tarea larga 2")
    cola.add("T3")
    cola.add("Tarea extensa 4")
    
    # Filtrar por tareas largas
    tareas_largas = cola.filter(lambda x: len(x) > 8)
    print(f"Tareas largas (>8 caracteres): {tareas_largas}")
    
    # Filtrar por tareas cortas
    tareas_cortas = cola.filter(lambda x: len(x) < 5)
    print(f"Tareas cortas (<5 caracteres): {tareas_cortas}")

if __name__ == '__main__':
    test_cola_limite_completo()
    test_contains()
    test_find()
    test_filter()
