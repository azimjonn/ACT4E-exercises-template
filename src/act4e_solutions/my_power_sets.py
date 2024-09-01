from typing import cast, Collection, Iterator, List, TypeVar
import act4e_interfaces as I

from .my_finite_sets import MyFiniteSet
from .sets_properties import SolFiniteSetProperties

C = TypeVar("C")

class MyFiniteSetOfFiniteSubsets(I.FiniteSetOfFiniteSubsets[C, MyFiniteSet[C]]):
    _subsets: List[MyFiniteSet[C]]

    def __init__(self, subsets: Collection[Collection[C]]):
        self._subsets = list(map(self.construct, subsets))

    def contents(self, e: MyFiniteSet[C]) -> Iterator[C]:
        return e.elements()
    def construct(self, elements: Collection[C]) -> MyFiniteSet[C]:
        return MyFiniteSet(elements)
    

    def elements(self) -> Iterator[MyFiniteSet[C]]:
        for sub in self._subsets:
            yield sub
    def size(self) -> int:
        return len(self._subsets)
    
    def contains(self, x: MyFiniteSet[C]) -> bool:
        dumb = SolFiniteSetProperties()
        for sub in self._subsets:
            if dumb.equal(sub, x):
                return True
            
        return False
    
    def load(self, h: I.IOHelper, o: I.ConcreteRepr) -> MyFiniteSet[C]:
        return super().load(h, o)
    def save(self, h: I.IOHelper, x: MyFiniteSet[C]) -> I.ConcreteRepr:
        return super().save(h, x)