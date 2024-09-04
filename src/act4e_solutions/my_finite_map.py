from typing import Sequence, Tuple, cast, Collection, Iterator, List, TypeVar, Mapping
import act4e_interfaces as I

from .my_finite_sets import MyFiniteSet
from .sets_properties import SolFiniteSetProperties

A = TypeVar("A")
B = TypeVar("B")

class MyFiniteMap(I.FiniteMap[A, B]):
    _source: I.FiniteSet[A]
    _target: I.FiniteSet[B]
    _mapping: Mapping[A, B]
    def __init__(self, source: I.FiniteSet[A], target: I.FiniteSet[B], mapping: Mapping[A, B]) -> None:
        self._source = source
        self._target = target
        self._mapping = mapping
    
    def source(self) -> I.FiniteSet[A]:
        return self._source
    def target(self) -> I.FiniteSet[B]:
        return self._target
    
    def __call__(self, a: A) -> B:
        for key, val in self._mapping:
            if key == a:
                return val