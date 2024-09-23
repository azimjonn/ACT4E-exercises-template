from typing import Sequence, Tuple, cast, Collection, Iterator, List, TypeVar, Mapping
import act4e_interfaces as I

from .my_finite_sets import MyFiniteSet
from .sets_properties import SolFiniteSetProperties

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