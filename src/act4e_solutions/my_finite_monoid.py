from typing import Sequence, Tuple, cast, Collection, Iterator, List, TypeVar, Mapping
import act4e_interfaces as I

from .my_finite_map import MyFiniteMap
from .my_finite_sets import MyFiniteSet
from .my_finite_set_product import MyFiniteSetProduct
from .my_finite_semigroup import MyFiniteSemigroup

A = TypeVar("A")
B = TypeVar("B")

class MyFiniteMonoid(I.FiniteMonoid[A], MyFiniteSemigroup[A]):
    _neutral: A
    def __init__(self, carrier: I.FiniteSet[A], composition: I.FiniteMap[B, A], neutral: A):
        super().__init__(carrier, composition)

        self._neutral = neutral

    def identity(self) -> A:
        return self._neutral