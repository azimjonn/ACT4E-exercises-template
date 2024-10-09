from typing import Any, overload, Sequence, TypeVar

import act4e_interfaces as I

X = TypeVar("X")

from .my_finite_posets import MyFinitePosetDisjointUnion

class SolFinitePosetConstructionSum(I.FinitePosetConstructionSum):
    def disjoint_union(self, ps: Sequence[I.FinitePoset[X]]) -> I.FinitePosetDisjointUnion[X, Any]:
        return MyFinitePosetDisjointUnion(ps)

