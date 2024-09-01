from typing import Any, Sequence, TypeVar

import act4e_interfaces as I

from .my_finite_set_product import MyFiniteSetProduct

X = TypeVar("X")


class SolFiniteMakeSetProduct(I.FiniteMakeSetProduct):

    def product(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetProduct[X, Any]:
        return MyFiniteSetProduct(components)
