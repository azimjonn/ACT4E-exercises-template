from typing import Any, Sequence, TypeVar

import act4e_interfaces as I

from .my_finite_set_disjoint_union import MyFiniteSetDisjointUnion

X = TypeVar("X")


class SolFiniteMakeSetDisjointUnion(I.FiniteMakeSetDisjointUnion):
    def disjoint_union(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetDisjointUnion[X, Any]:
        return MyFiniteSetDisjointUnion(components)
