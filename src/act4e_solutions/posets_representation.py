from typing import Any, cast
import act4e_interfaces as I

from .my_finite_posets import MyFinitePoset
from .posets_product import SolFinitePosetConstructionProduct
from .posets_sum import SolFinitePosetConstructionSum

from .sets_representation import MyFiniteSetRepresentation
from .relations_representation import SolFiniteRelationRepresentation
from .relations import SolFiniteEndorelationOperations

class SolFinitePosetRepresentation(I.FinitePosetRepresentation):
    def load(self, h: I.IOHelper, s: I.FinitePoset_desc) -> I.FinitePoset[Any]:
        if "poset_product" in s:
            pp_desc = s["poset_product"]
            
            comps = [self.load(s, p) for p in pp_desc]

            return SolFinitePosetConstructionProduct().product(comps)
        
        if "poset_sum" in s:
            ps_desc = s["poset_sum"]
            
            comps = [self.load(s, p) for p in ps_desc]

            return SolFinitePosetConstructionSum().disjoint_union(comps)

        carrier = MyFiniteSetRepresentation().load(h, s["carrier"])

        temp_relation = {"source": s["carrier"], "target": s["carrier"], "values": s["hasse"]}
        partial_relation = SolFiniteRelationRepresentation().load(h, temp_relation)
        full_relation = SolFiniteEndorelationOperations().transitive_closure(partial_relation, fill_reflex=True)

        return MyFinitePoset(carrier, full_relation)


    def save(self, h: I.IOHelper, p: I.FinitePoset[Any]) -> I.FinitePoset_desc:
        if isinstance(p, I.FinitePosetProduct):
            pass

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
