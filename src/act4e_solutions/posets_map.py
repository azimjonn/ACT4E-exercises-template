from typing import TypeVar

import act4e_interfaces as I

A = TypeVar("A")
B = TypeVar("B")
X = TypeVar("X")

from .posets_bounds import SolFinitePosetConstructionOpposite

class SolFiniteMonotoneMapProperties(I.FiniteMonotoneMapProperties):
    def is_monotone(self, p1: I.FinitePoset[A], p2: I.FinitePoset[B], m: I.FiniteMap[A, B]) -> bool:
        for x in p1.carrier().elements():
            for y in p1.carrier().elements():
                if p1.holds(x, y):
                    if not p2.holds(m(x), m(y)):
                        return False
        
        return True

    def is_antitone(self, p1: I.FinitePoset[A], p2: I.FinitePoset[B], m: I.FiniteMap[A, B]) -> bool:
        return self.is_monotone(SolFinitePosetConstructionOpposite().opposite(p1), p2, m)
