from typing import Any, TypeVar

import act4e_interfaces as I

from .my_finite_sets import MyFiniteSet
from .my_finite_map import MyFiniteMap
from .sets_representation import MyFiniteSetRepresentation

A = TypeVar("A")
B = TypeVar("B")


class SolFiniteMapRepresentation(I.FiniteMapRepresentation):
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
        
        mapping = []
        for pair in values:
            key = source.load(h, pair[0])
            val = target.load(h, pair[1])
            if any(key == existing_key for existing_key, _ in mapping):
                raise I.InvalidFormat()
            
            mapping.append((key, val))
        
        return MyFiniteMap(source, target, mapping)

    def save(self, h: I.IOHelper, m: I.FiniteMap[A, B]) -> I.FiniteMap_desc:
        values = []
        for key in m.source().elements():
            val = m(key)
            values.append([key, val])

        result = {
            "source": self.setRepresentation.save(h, m.source()),
            "target": self.setRepresentation.save(h, m.target()),
            "values": values
        }

        return result