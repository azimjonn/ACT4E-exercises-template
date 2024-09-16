from typing import List, TypeVar

import act4e_interfaces as I

from .my_finite_semigroups import MyFreeSemigroup

C = TypeVar("C")

class SolFiniteSemigroupConstruct(I.FiniteSemigroupConstruct):
    def free(self, fs: I.FiniteSet[C]) -> I.FreeSemigroup[C, List[C]]:
        return MyFreeSemigroup(fs)
