from typing import Any, TypeVar

import act4e_interfaces as I

from .my_finite_set_product import MyFiniteSetProduct
from .my_finite_semigroup import MyFiniteSemigroup

from .sets_representation import MyFiniteSetRepresentation
from .maps_representation import SolFiniteMapRepresentation

X = TypeVar("X")


class SolFiniteSemigroupRepresentation(I.FiniteSemigroupRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteSemigroup_desc) -> I.FiniteSemigroup[X]:
        carrier = MyFiniteSetRepresentation().load(h, s["carrier"])
        
        source = MyFiniteSetProduct((carrier, carrier))
        target = carrier
        values = s["composition"]
        map_repr = {
            "source": MyFiniteSetRepresentation().save(h, source),
            "target": MyFiniteSetRepresentation().save(h, target),
            "values": values
        }

        composition = SolFiniteMapRepresentation().load(h, map_repr)
        
        return MyFiniteSemigroup(carrier, composition)

    def save(self, h: I.IOHelper, m: I.FiniteSemigroup[X]) -> I.FiniteSemigroup_desc:
        carrier = m.carrier()

        composition = []
        for elem in MyFiniteSetProduct((carrier, carrier)).elements():
            composition.append([elem, m.compose(*elem)])
        repr = {
            "carrier": MyFiniteSetRepresentation().save(h, carrier),
            "composition": composition
        }
        
        return repr


class SolFiniteMonoidRepresentation(I.FiniteMonoidRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteMonoid_desc) -> I.FiniteMonoid[X]:
        raise NotImplementedError()

    def save(self, h: I.IOHelper, m: I.FiniteMonoid[Any]) -> I.FiniteMonoid_desc:
        raise NotImplementedError()


class SolFiniteGroupRepresentation(I.FiniteGroupRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteGroup_desc) -> I.FiniteGroup[X]:
        raise NotImplementedError()

    def save(self, h: I.IOHelper, m: I.FiniteGroup[Any]) -> I.FiniteGroup_desc:
        raise NotImplementedError()
