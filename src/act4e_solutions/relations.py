from typing import Any, TypeVar

import act4e_interfaces as I
from act4e_interfaces import FiniteRelation

from .my_finite_relation import MyFiniteRelation

E1 = TypeVar("E1")
E2 = TypeVar("E2")
E3 = TypeVar("E3")
E = TypeVar("E")

A = TypeVar("A")
B = TypeVar("B")


class SolFiniteRelationProperties(I.FiniteRelationProperties):
    def is_surjective(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_defined_everywhere(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_injective(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_single_valued(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()


class SolFiniteRelationOperations(I.FiniteRelationOperations):
    def transpose(self, fr: I.FiniteRelation[A, B]) -> I.FiniteRelation[B, A]:
        raise NotImplementedError()

    def as_relation(self, f: I.FiniteMap[A, B]) -> I.FiniteRelation[A, B]:
        raise NotImplementedError()


class SolFiniteEndorelationProperties(I.FiniteEndorelationProperties):
    def is_reflexive(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_irreflexive(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_transitive(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_symmetric(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_antisymmetric(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_asymmetric(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()


class SolFiniteEndorelationOperations(I.FiniteEndorelationOperations):
    def transitive_closure(self, fr: I.FiniteRelation[E, E]) -> I.FiniteRelation[E, E]:
        raise NotImplementedError()


class SolFiniteRelationCompose(I.FiniteRelationCompose):
    def compose(self, fr1: FiniteRelation[E1, E2], fr2: FiniteRelation[E2, E3]) -> I.FiniteRelation[E1, E3]:
        pairs = []
        for a in fr1.source().elements():
            for b in fr1.target().elements():
                if not fr1.holds(a, b):
                    continue
                
                for c in fr2.target().elements():
                    if fr2.holds(b, c):
                        pairs.append((a, c))
        
        return MyFiniteRelation(fr1.source(), fr2.target(), pairs)