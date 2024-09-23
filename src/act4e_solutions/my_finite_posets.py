from typing import Sequence, Tuple, cast, Collection, Iterator, List, TypeVar, Mapping
import act4e_interfaces as I

from .my_finite_sets import MyFiniteSet
from .sets_properties import SolFiniteSetProperties
from .sets_power import SolFiniteMakePowerSet

A = TypeVar("A")
B = TypeVar("B")

class MyFinitePoset(I.FinitePoset[A]):
    _carrier: I.FiniteSet[A]
    _relation: I.FiniteRelation[A, A]
    def __init__(self, carrier: I.FiniteSet[A], relation: I.FiniteRelation[A, A]):
        self._carrier = carrier
        self._relation = relation

    def carrier(self) -> I.FiniteSet[A]:
        return self._carrier
    
    def holds(self, a: A, b: A) -> bool:
        return self._relation.holds(a, b)

class MyFinitePosetOfFiniteSubsets(I.FinitePosetOfFiniteSubsets[A, I.FiniteSet[A]]):
    _base: I.FiniteSet[A]

    def __init__(self, base: I.FiniteSet[A]) -> None:
        self._base = base

    def carrier(self) -> I.FiniteSetOfFiniteSubsets[A, I.FiniteSet[A]]:
        return SolFiniteMakePowerSet().powerset(self._base)
    
    def holds(self, a: I.FiniteSet[A], b: I.FiniteSet[A]) -> bool:
        return SolFiniteSetProperties().is_subset(a, b)