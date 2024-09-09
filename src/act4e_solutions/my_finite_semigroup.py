from typing import Sequence, Tuple, cast, Collection, Iterator, List, TypeVar, Mapping
import act4e_interfaces as I

from .my_finite_map import MyFiniteMap
from .my_finite_sets import MyFiniteSet
from .my_finite_set_product import MyFiniteSetProduct

A = TypeVar("A")
B = TypeVar("B")

class MyFiniteSemigroup(I.FiniteSemigroup[A]):
    _carrier: MyFiniteSet[A]
    _composition: MyFiniteMap[Tuple[A, A], A]

    def __init__(self, carrier: I.FiniteSet[A], composition):
        self._carrier = carrier
        self._composition = composition

    def carrier(self) -> I.FiniteSet[A]:
        return self._carrier
    def compose(self, a: A, b: A) -> A:
        return self._composition([a, b])
    