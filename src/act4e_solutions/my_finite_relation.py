from typing import Sequence, Tuple, cast, Collection, Iterator, List, TypeVar, Mapping
import act4e_interfaces as I

from .my_finite_sets import MyFiniteSet
from .sets_properties import SolFiniteSetProperties

A = TypeVar("A")
B = TypeVar("B")

class MyFiniteRelation(I.FiniteRelation[A, B]):
    _source: I.FiniteSet[A]
    _target: I.FiniteSet[B]
    _pairs: List[Tuple[A, B]]
    def __init__(self, source: I.FiniteSet[A], target: I.FiniteSet[B], pairs: List[Tuple[A, B]]) -> None:
        self._source = source
        self._target = target
        self._pairs = pairs
    
    def source(self) -> I.FiniteSet[A]:
        return self._source
    def target(self) -> I.FiniteSet[B]:
        return self._target
    
    def holds(self, e1: A, e2: B) -> bool:
        return (e1, e2) in self._pairs