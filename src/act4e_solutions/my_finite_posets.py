from typing import Sequence, Tuple, cast, Collection, Iterator, List, TypeVar, Mapping
import act4e_interfaces as I

from .my_finite_sets import MyFiniteSet
from .sets_properties import SolFiniteSetProperties
from .sets_power import SolFiniteMakePowerSet
from .my_finite_set_product import MyFiniteSetProduct
from .my_finite_set_disjoint_union import MyFiniteSetDisjointUnion

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")

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

class MyFinitePosetProduct(I.FinitePosetProduct[C, List[C]]):
    _components: List[I.FinitePoset[C]]
    _carrier: I.FiniteSetProduct[C, List[C]]
    def __init__(self, ps: Sequence[I.FinitePoset[C]]) -> None:
        self._components = ps

        fs = [c.carrier() for c in ps]
        self._carrier = MyFiniteSetProduct(fs)
    
    def carrier(self) -> I.FiniteSetProduct[C, List[C]]:
        return self._carrier

    def components(self) -> Sequence[I.FinitePoset[C]]:
        return self._components
    
    def holds(self, a: List[C], b: List[C]) -> bool:
        for ai, bi, poset in zip(a, b, self._components):
            if not poset.holds(ai, bi):
                return False
        
        return True

class MyFinitePosetDisjointUnion(I.FinitePosetDisjointUnion[C, Tuple[int, C]]):
    _components: List[I.FinitePoset[C]]
    _carrier: I.FiniteSetDisjointUnion[C, Tuple[int, C]]

    def __init__(self, ps: Collection[I.FinitePoset[C]]):
        self._components = list(ps)

        fs = [c.carrier() for c in self._components]
        self._carrier = MyFiniteSetDisjointUnion(fs)
    
    def components(self) -> Sequence[I.FinitePoset[C]]:
        return self._components
    
    def carrier(self) -> I.FiniteSetDisjointUnion[C, Tuple[int | C]]:
        return self._carrier
    
    def holds(self, a: Tuple[int, C], b: Tuple[int, C]) -> bool:
        if a[0] != b[0]:
            return False
        
        return self._components[a[0] - 1].holds(a[1], b[1])