from typing import Any, TypeVar, cast

from .my_finite_morphisms import MyFiniteGroupMorphism, MyFiniteSemigroupMorphism, MyFiniteMonoidMorphism

from .semigroups_representation import SolFiniteSemigroupRepresentation, SolFiniteMonoidRepresentation, SolFiniteGroupRepresentation
from .maps_representation import SolFiniteMapRepresentation

import act4e_interfaces as I

class SolFiniteSemigroupMorphismRepresentation(I.FiniteSemigroupMorphismRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteSemigroupMorphism_desc) -> I.FiniteSemigroupMorphism[Any, Any]:
        source = SolFiniteSemigroupRepresentation().load(h, s["source"])
        target = SolFiniteSemigroupRepresentation().load(h, s["target"])
        mapping = SolFiniteMapRepresentation().load(h, s["mapping"])

        return MyFiniteSemigroupMorphism(source, target, mapping)

    def save(self, h: I.IOHelper, m: I.FiniteSemigroupMorphism[Any, Any]) -> I.FiniteSemigroupMorphism_desc:
        repr = {
            "source": SolFiniteSemigroupRepresentation().save(h, m.source()),
            "target": SolFiniteSemigroupRepresentation().save(h, m.target()),
            "mapping": SolFiniteMapRepresentation().save(h, m.mapping())
        }

        return cast(I.FiniteSemigroupMorphism_desc, repr)


class SolFiniteMonoidMorphismRepresentation(I.FiniteMonoidMorphismRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteMonoidMorphism_desc) -> I.FiniteMonoidMorphism[Any, Any]:
        source = SolFiniteMonoidRepresentation().load(h, s["source"])
        target = SolFiniteMonoidRepresentation().load(h, s["target"])
        mapping = SolFiniteMapRepresentation().load(h, s["mapping"])

        return MyFiniteMonoidMorphism(source, target, mapping)

    def save(self, h: I.IOHelper, m: I.FiniteMonoidMorphism[Any, Any]) -> I.FiniteMonoidMorphism_desc:
        repr = {
            "source": SolFiniteMonoidRepresentation().save(h, m.source()),
            "target": SolFiniteMonoidRepresentation().save(h, m.target()),
            "mapping": SolFiniteMapRepresentation().save(h, m.mapping())
        }

        return cast(I.FiniteMonoidMorphism_desc, repr)


class SolFiniteGroupMorphismRepresentation(I.FiniteGroupMorphismRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteGroupMorphism_desc) -> I.FiniteGroupMorphism[Any, Any]:
        source = SolFiniteGroupRepresentation().load(h, s["source"])
        target = SolFiniteGroupRepresentation().load(h, s["target"])
        mapping = SolFiniteMapRepresentation().load(h, s["mapping"])

        return MyFiniteGroupMorphism(source, target, mapping)

    def save(self, h: I.IOHelper, m: I.FiniteGroupMorphism[Any, Any]) -> I.FiniteGroupMorphism_desc:
        repr = {
            "source": SolFiniteGroupRepresentation().save(h, m.source()),
            "target": SolFiniteGroupRepresentation().save(h, m.target()),
            "mapping": SolFiniteMapRepresentation().save(h, m.mapping())
        }

        return cast(I.FiniteGroupMorphism_desc, repr)
