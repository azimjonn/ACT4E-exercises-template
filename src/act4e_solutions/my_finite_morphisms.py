from typing import TypeVar
import act4e_interfaces as I

A = TypeVar("A")
B = TypeVar("B")

class MyFiniteSemigroupMorphism(I.FiniteSemigroupMorphism[A, B]):
    _source: I.FiniteSemigroup[A]
    _target: I.FiniteSemigroup[B]
    _mapping: I.FiniteMap[A, B]
    def __init__(self, source: I.FiniteSemigroup[A], target: I.FiniteSemigroup[B], mapping: I.FiniteMap[A, B]):
        self._source = source
        self._target = target
        self._mapping = mapping
    
    def source(self) -> I.FiniteSemigroup[A]:
        return self._source
    
    def target(self) -> I.FiniteSemigroup[B]:
        return self._target
    
    def mapping(self) -> I.FiniteMap[A, B]:
        return self._mapping

class MyFiniteMonoidMorphism(I.FiniteMonoidMorphism[A, B]):
    _source: I.FiniteMonoid[A]
    _target: I.FiniteMonoid[B]
    _mapping: I.FiniteMap[A, B]
    def __init__(self, source: I.FiniteMonoid[A], target: I.FiniteMonoid[B], mapping: I.FiniteMap[A, B]):
        self._source = source
        self._target = target
        self._mapping = mapping
    
    def source(self) -> I.FiniteMonoid[A]:
        return self._source
    
    def target(self) -> I.FiniteMonoid[B]:
        return self._target
    
    def mapping(self) -> I.FiniteMap[A, B]:
        return self._mapping

class MyFiniteGroupMorphism(I.FiniteGroupMorphism[A, B]):
    _source: I.FiniteGroup[A]
    _target: I.FiniteGroup[B]
    _mapping: I.FiniteMap[A, B]
    def __init__(self, source: I.FiniteGroup[A], target: I.FiniteGroup[B], mapping: I.FiniteMap[A, B]):
        self._source = source
        self._target = target
        self._mapping = mapping
    
    def source(self) -> I.FiniteGroup[A]:
        return self._source
    
    def target(self) -> I.FiniteGroup[B]:
        return self._target
    
    def mapping(self) -> I.FiniteMap[A, B]:
        return self._mapping