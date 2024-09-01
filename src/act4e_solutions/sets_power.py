from typing import Any, overload, TypeVar

import act4e_interfaces as I

from .my_power_sets import MyFiniteSetOfFiniteSubsets

X = TypeVar("X")


class SolFiniteMakePowerSet(I.FiniteMakePowerSet):
    def powerset(self, s: I.FiniteSet[X]) -> I.FiniteSetOfFiniteSubsets[X, Any]:
        elements = list(s.elements())
        subsets = self._generate_subsets(elements)

        return MyFiniteSetOfFiniteSubsets(subsets)
    
    def _generate_subsets(self, seq):
        if len(seq) == 0:
            return [[]]
        
        tail_subsets = self._generate_subsets(seq[1:])

        new_subsets = []
        for sub in tail_subsets:
            new_subsets.append([seq[0]] + sub)
        
        return new_subsets + tail_subsets