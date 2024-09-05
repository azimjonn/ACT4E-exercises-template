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
        return all(any(fr.holds(a, b) for a in fr.source().elements()) for b in fr.target().elements())

    def is_defined_everywhere(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        return all(any(fr.holds(a, b) for b in fr.target().elements()) for a in fr.source().elements())

    def is_injective(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        return not any(sum(fr.holds(a, b) for a in fr.source().elements()) > 1 for b in fr.target().elements())

    def is_single_valued(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        return not any(sum(fr.holds(a, b) for b in fr.target().elements()) > 1 for a in fr.source().elements())


class SolFiniteRelationOperations(I.FiniteRelationOperations):
    def transpose(self, fr: I.FiniteRelation[A, B]) -> I.FiniteRelation[B, A]:
        pairs = []

        for a in fr.source().elements():
            for b in fr.target().elements():
                if fr.holds(a, b):
                    pairs.append((b, a))
        
        return MyFiniteRelation(fr.target(), fr.source(), pairs)

    def as_relation(self, f: I.FiniteMap[A, B]) -> I.FiniteRelation[A, B]:
        pairs = [(a, f(a)) for a in f.source().elements()]

        return MyFiniteRelation(f.source(), f.target(), pairs)


class SolFiniteEndorelationProperties(I.FiniteEndorelationProperties):
    def is_reflexive(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        return all(fr.holds(a, a) for a in fr.source().elements())

    def is_irreflexive(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        return not any(fr.holds(a, a) for a in fr.source().elements())

    def is_transitive(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        for a in fr.source().elements():
            for b in fr.source().elements():
                for c in fr.source().elements():
                    if fr.holds(a, b) and fr.holds(b, c):
                        if not fr.holds(a, c):
                            return False

        return True

    def is_symmetric(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        for a in fr.source().elements():
            for b in fr.source().elements():
                if fr.holds(a, b):
                    if not fr.holds(b, a):
                        return False
        
        return True

    def is_antisymmetric(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        for a in fr.source().elements():
            for b in fr.source().elements():
                if fr.holds(a, b) and fr.holds(b, a):
                    return a == b
        return False

    def is_asymmetric(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        for a in fr.source().elements():
            for b in fr.source().elements():
                if fr.holds(a, b):
                    if fr.holds(b, a):
                        return False
        
        return True


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