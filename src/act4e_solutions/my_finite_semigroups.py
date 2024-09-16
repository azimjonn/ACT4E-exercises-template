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

    def __init__(self, carrier: I.FiniteSet[A], composition: I.FiniteMap[B, A]):
        self._carrier = carrier
        self._composition = composition

    def carrier(self) -> I.FiniteSet[A]:
        return self._carrier
    def compose(self, a: A, b: A) -> A:
        return self._composition([a, b])

class MyFreeSemigroup(I.FreeSemigroup[A, List[A]]):
    _carrier: I.FiniteSet[A]

    def __init__(self, carrier: I.FiniteSet[A]):
        self._carrier = carrier

    def carrier(self) -> I.FiniteSet[A]:
        return self._carrier
    
    def compose(self, a: List[A], b: List[A]) -> List[A]:
        return a + b

    def unit(self, a: A) -> List[A]:
        return [a]

class MyFiniteMonoid(I.FiniteMonoid[A], MyFiniteSemigroup[A]):
    _neutral: A
    def __init__(self, carrier: I.FiniteSet[A], composition: I.FiniteMap[B, A], neutral: A):
        super().__init__(carrier, composition)

        self._neutral = neutral

    def identity(self) -> A:
        return self._neutral

class MyFiniteGroup(I.FiniteGroup[A], MyFiniteMonoid[A]):
    _inverse: MyFiniteMap[Tuple[A, A], A]
    def __init__(self, carrier: I.FiniteSet[A], composition: I.FiniteMap[B, A], neutral: A, inverse: I.FiniteMap[A, A]):
        super().__init__(carrier, composition, neutral)
        
        self._inverse = inverse
    
    def inverse(self, e: A) -> A:
        return self._inverse(e)