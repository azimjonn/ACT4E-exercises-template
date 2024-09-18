from typing import Any, TypeVar

import act4e_interfaces as I

from itertools import product, chain

A = TypeVar("A")
B = TypeVar("B")


class SolFiniteSemigroupMorphismsChecks(I.FiniteSemigroupMorphismsChecks):
    def is_semigroup_morphism(self, a: I.FiniteSemigroup[A], b: I.FiniteSemigroup[B], f: I.FiniteMap[A, B]) -> bool:
        return all(f(a.compose(x, y)) == b.compose(f(x), f(y)) for x, y in product(a.carrier().elements(), a.carrier().elements()))

    def is_monoid_morphism(self, a: I.FiniteMonoid[A], b: I.FiniteMonoid[B], f: I.FiniteMap[A, B]) -> bool:
        return all(chain([f(a.identity()) == b.identity()], (f(a.compose(x, y)) == b.compose(f(x), f(y)) for x, y in product(a.carrier().elements(), a.carrier().elements()))))

    def is_group_morphism(self, a: I.FiniteGroup[A], b: I.FiniteGroup[B], f: I.FiniteMap[A, B]) -> bool:
        return self.is_semigroup_morphism(a, b, f)
