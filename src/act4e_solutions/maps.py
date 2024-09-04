from typing import TypeVar

import act4e_interfaces as I

from .my_finite_map import MyFiniteMap

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")


class SolFiniteMapOperations(I.FiniteMapOperations):

    def identity(self, s: I.FiniteSet[A]) -> I.Mapping[A, A]:
        mapping = [(key, key) for key in s.elements()]

        return MyFiniteMap(s, s, mapping)

    def compose(self, f: I.FiniteMap[A, B], g: I.FiniteMap[B, C]) -> I.FiniteMap[A, C]:
        mapping = [(key, g(f(key))) for key in f.source().elements()]

        return MyFiniteMap(f.source(), g.target(), mapping)
