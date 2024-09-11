from typing import Any

import act4e_interfaces as I

from .my_finite_sets import MyFiniteSet
from .my_finite_set_product import MyFiniteSetProduct

class MyFiniteSetRepresentation(I.FiniteSetRepresentation):
    def load(self, h: I.IOHelper, data: I.FiniteSet_desc) -> I.FiniteSet[Any]:
        if not isinstance(data, dict):
            raise I.InvalidFormat()
        if "elements" in data:
            if not isinstance(data["elements"], list):
                raise I.InvalidFormat()
            elements = data["elements"]
            return MyFiniteSet(elements)
        elif "product" in data:
            if not isinstance(data["product"], list):
                raise I.InvalidFormat()
            components = [self.load(h, comp) for comp in data["product"]]
            return MyFiniteSetProduct(components)
        else:
            raise I.InvalidFormat()

    def save(self, h: I.IOHelper, f: I.FiniteSet[Any]) -> I.FiniteSet_desc:
        if isinstance(f, I.FiniteSetProduct):
            result = [self.save(h, x) for x in f.components()]
            return {"product": result}
        
        elif isinstance(f, I.FiniteSet):
            all_elements = [f.save(h, elem) for elem in f.elements()]
            return {"elements": all_elements}
            