from typing import TypeVar

import act4e_interfaces as I

from .my_finite_relation import MyFiniteRelation
from .sets_representation import MyFiniteSetRepresentation

A = TypeVar("A")
B = TypeVar("B")


class SolFiniteRelationRepresentation(I.FiniteRelationRepresentation):
    setRepresentation = MyFiniteSetRepresentation()
    def load(self, h: I.IOHelper, s: I.FiniteMap_desc) -> I.FiniteMap[A, B]:
        if not isinstance(s, dict):
            raise I.InvalidFormat()
        
        if not all(map(lambda x: x in s, ["source", "target", "values"])):
            raise I.InvalidFormat()
        
        source = self.setRepresentation.load(h, s["source"])
        target = self.setRepresentation.load(h, s["target"])
        values = s["values"]

        if not isinstance(values, list):
            raise I.InvalidFormat()
        
        pairs = []
        for pair in values:
            key = source.load(h, pair[0])
            val = target.load(h, pair[1])
            
            pairs.append((key, val))
        
        return MyFiniteRelation(source, target, pairs)

    def save(self, h: I.IOHelper, r: I.FiniteRelation[A, B]) -> I.FiniteMap_desc:
        values = []
        for s in r.source().elements():
            for t in r.target().elements():
                if r.holds(s, t):
                    values.append([s, t])

        result = {
            "source": self.setRepresentation.save(h, r.source()),
            "target": self.setRepresentation.save(h, r.target()),
            "values": values
        }

        return result
