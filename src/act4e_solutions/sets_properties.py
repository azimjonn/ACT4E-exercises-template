from typing import Any, overload, Sequence, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolFiniteSetProperties(I.FiniteSetProperties):
    def is_subset(self, a: I.FiniteSet[X], b: I.FiniteSet[X]) -> bool:
        for elem in a.elements():
            if not b.contains(elem):
                return False
        
        return True


class SolFiniteMakeSetUnion(I.FiniteMakeSetUnion):
    def union(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetUnion[X, Any]:
        raise NotImplementedError() # implement here


class SolFiniteMakeSetIntersection(I.FiniteMakeSetIntersection):
    def intersection(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSet[X]:
        raise NotImplementedError()
