from typing import Any, cast
import act4e_interfaces as I

from .my_finite_posets import MyFinitePoset

from .sets_representation import MyFiniteSetRepresentation
from .relations_representation import SolFiniteRelationRepresentation
from .relations import SolFiniteEndorelationOperations

class SolFinitePosetRepresentation(I.FinitePosetRepresentation):
    def load(self, h: I.IOHelper, s: I.FinitePoset_desc) -> I.FinitePoset[Any]:
        if not all(map(lambda x: x in s, ["carrier", "hasse"])):
            raise I.InvalidFormat()

        carrier = MyFiniteSetRepresentation().load(h, s["carrier"])

        temp_relation = {"source": s["carrier"], "target": s["carrier"], "values": s["hasse"]}
        partial_relation = SolFiniteRelationRepresentation().load(h, temp_relation)
        full_relation = SolFiniteEndorelationOperations().transitive_closure(partial_relation, fill_reflex=True)

        return MyFinitePoset(carrier, full_relation)


    def save(self, h: I.IOHelper, p: I.FinitePoset[Any]) -> I.FinitePoset_desc:
        pairs = []
        for x in p.carrier().elements():
            for y in p.carrier().elements():
                if x == y: continue

                if p.holds(x, y):
                    pairs.append([x, y])
        repr = {
            "carrier": MyFiniteSetRepresentation().save(h, p.carrier()),
            "hasse": pairs
        }

        return cast(I.FinitePoset_desc, repr)
