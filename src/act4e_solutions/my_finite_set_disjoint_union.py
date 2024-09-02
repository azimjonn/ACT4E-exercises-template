from typing import Sequence, Tuple, cast, Collection, Iterator, List, TypeVar
import act4e_interfaces as I

from .my_finite_sets import MyFiniteSet
from .sets_properties import SolFiniteSetProperties

C = TypeVar("C")

class MyFiniteSetDisjointUnion(I.FiniteSetDisjointUnion[C, Tuple[int, C]]):
    _components: List[MyFiniteSet[C]]
    def __init__(self, components: Collection[I.FiniteSet[C]]):
        self._components = components
    
    def pack(self, i: int, e: C) -> Tuple[int, C]:
        if i < 1 or i > len(self._components):
            raise I.InvalidValue()
        if not self._components[i - 1].contains(e):
            raise I.InvalidValue()
        
        return (i, e)
    def unpack(self, e: Tuple[int, C]) -> Tuple[int, C]:
        return e
    
    def size(self) -> int:
        return sum(map(lambda x: x.size(), self._components))
    def contains(self, x: Tuple[int, C]) -> bool:
        i, e = x
        if i < 1 or i > len(self._components):
            return False
        
        return self._components[i].contains(e)
    def components(self) -> Sequence[I.FiniteSet[C]]:
        return self.components()
    def elements(self) -> Iterator[Tuple[int, C]]:
        for idx, comp in enumerate(self._components):
            for elem in comp.elements():
                yield (idx + 1, elem)
    
    def load(self, h: I.IOHelper, o: I.ConcreteRepr) -> Tuple[int | C]:
        return super().load(h, o)
    def save(self, h: I.IOHelper, x: Tuple[int | C]) -> I.ConcreteRepr:
        return super().save(h, x)