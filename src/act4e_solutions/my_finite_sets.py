from typing import cast, Collection, Iterator, List, TypeVar

import act4e_interfaces as I

E = TypeVar("E")

class MyFiniteSet(I.FiniteSet[E]):
    _elements: List[E]

    def __init__(self, elements: Collection[E]):
        self._elements = list(elements)
    
    def size(self) -> int:
        return len(self._elements)
    
    def contains(self, x: E) -> bool:
        return x in self._elements

    def elements(self) -> Iterator[E]:
        for elem in self._elements:
            yield elem
    
    def save(self, h: I.IOHelper, x: E) -> I.ConcreteRepr:
        return cast(I.ConcreteRepr, x)
    
    def load(self, h: I.IOHelper, o: I.ConcreteRepr) -> E:
        return cast(E, o)