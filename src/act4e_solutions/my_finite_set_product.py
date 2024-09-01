from typing import Sequence, cast, Collection, Iterator, List, TypeVar
import act4e_interfaces as I

from .my_finite_sets import MyFiniteSet
from .sets_properties import SolFiniteSetProperties

C = TypeVar("C")

class MyFiniteSetProduct(I.FiniteSetProduct[C, List[C]]):
    _components: List[I.FiniteSet[C]]
    def __init__(self, components: Sequence[I.FiniteSet[C]]):
        self._components = list(components)

    def components(self) -> Sequence[I.FiniteSet[C]]:
        return self._components
    
    def contains(self, x: List[C]) -> bool:
        if not isinstance(x, List):
            return False
        for elem, comp in zip(x, self._components):
            if not comp.contains(elem):
                return False
        
        return True

    def size(self) -> int:
        ans = 1
        for c in self._components:
            ans *= c.size()
        return ans
    
    def elements(self) -> Iterator[List[C]]:
        result = [[]]

        for comp in self._components:
            temp_result = []

            for item in result:
                for elem in comp.elements():
                    temp_result.append(item + [elem])
            result = temp_result
        
        for product in result:
            yield product
    
    def pack(self, args: Sequence[C]) -> List[C]:
        return list(args)
    def unpack(self, args: List[C]) -> Sequence[C]:
        return args

    def load(self, h: I.IOHelper, o: I.ConcreteRepr) -> List[C]:
        return cast(List[C], o)
    def save(self, h: I.IOHelper, x: List[C]) -> I.ConcreteRepr:
        return cast(I.ConcreteRepr, x)