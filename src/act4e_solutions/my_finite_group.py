from typing import Sequence, Tuple, cast, Collection, Iterator, List, TypeVar, Mapping
import act4e_interfaces as I

from .my_finite_map import MyFiniteMap
from .my_finite_monoid import MyFiniteMonoid

from .maps import SolFiniteMapOperations

A = TypeVar("A")
B = TypeVar("B")

class MyFiniteGroup(I.FiniteGroup[A], MyFiniteMonoid[A]):
    _inverse: MyFiniteMap[Tuple[A, A], A]
    def __init__(self, carrier: I.FiniteSet[A], composition: I.FiniteMap[B, A], neutral: A, inverse: I.FiniteMap[A, A]):
        super().__init__(carrier, composition, neutral)
        
        self._inverse = inverse
    
    def inverse(self, e: A) -> A:
        return self._inverse(e)