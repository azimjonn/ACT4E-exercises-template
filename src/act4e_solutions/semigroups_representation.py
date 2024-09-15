from typing import Any, TypeVar

import act4e_interfaces as I

from .my_finite_set_product import MyFiniteSetProduct
from .my_finite_semigroup import MyFiniteSemigroup
from .my_finite_monoid import MyFiniteMonoid
from .my_finite_group import MyFiniteGroup

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
        semigroup = SolFiniteSemigroupRepresentation().load(h, s)
        neutral = s["neutral"]

        return MyFiniteMonoid(semigroup.carrier(), semigroup._composition, neutral) # not good

    def save(self, h: I.IOHelper, m: I.FiniteMonoid[Any]) -> I.FiniteMonoid_desc:
        semigroup = SolFiniteSemigroupRepresentation().save(h, m)
        semigroup["neutral"] = m.identity()

        return semigroup


class SolFiniteGroupRepresentation(I.FiniteGroupRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteGroup_desc) -> I.FiniteGroup[X]:
        monoid = SolFiniteMonoidRepresentation().load(h, s)

        map_repr = {
            "source": MyFiniteSetRepresentation().save(h, monoid.carrier()),
            "target": MyFiniteSetRepresentation().save(h, monoid.carrier()),
            "values": s["inverse"]
        }
        inverse = SolFiniteMapRepresentation().load(h, map_repr)

        return MyFiniteGroup(
            monoid.carrier(),
            monoid._composition,
            monoid.identity(),
            inverse
        )

    def save(self, h: I.IOHelper, m: I.FiniteGroup[Any]) -> I.FiniteGroup_desc:
        monoid = SolFiniteMonoidRepresentation().save(h, m)
        monoid["inverse"] = [[x, m.inverse(x)] for x in m.carrier().elements()]

        return monoid