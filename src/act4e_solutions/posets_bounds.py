from typing import Any, List, Optional, overload, TypeVar, Collection

import act4e_interfaces as I

import copy

E = TypeVar("E")
X = TypeVar("X")

class SolFinitePosetMeasurement(I.FinitePosetMeasurement):
    def height(self, fp: I.FinitePoset[Any]) -> int:
        min_elems = []
        for x in fp.carrier().elements():
            if not any(x != y and fp.holds(y, x) for y in fp.carrier().elements()):
                min_elems.append(x)
        
        visited = set(min_elems)
        h = 1
        while True:
            next_layer = set()
            for x in fp.carrier().elements():
                if x in visited:
                    continue
                
                predecessors = {y for y in fp.carrier().elements() if fp.holds(y, x) and y != x}
                if predecessors.issubset(visited):
                    next_layer.add(x)

            if not next_layer:
                break

            visited.update(next_layer)
            h += 1
        
        return h

    def width(self, fp: I.FinitePoset[Any]) -> int:
        return 0


class SolFinitePosetConstructionOpposite(I.FinitePosetConstructionOpposite):
    def opposite(self, p: I.FinitePoset[X]) -> I.FinitePoset[X]:
        op = copy.deepcopy(p)
        op.holds = lambda x, y: p.holds(y, x)

        return op


class SolFinitePosetSubsetProperties(I.FinitePosetSubsetProperties):
    def is_chain(self, fp: I.FinitePoset[X], s: Collection[X]) -> bool:
        for x in s:
            for y in s:
                if not (fp.holds(x, y) or fp.holds(y, x)):
                    return False
        
        return True

    def is_antichain(self, fp: I.FinitePoset[X], s: Collection[X]) -> bool:
        for x in s:
            for y in s:
                if x == y: continue

                if fp.holds(x, y) or fp.holds(y, x):
                    return False
        
        return True


class SolFinitePosetSubsetProperties2(I.FinitePosetSubsetProperties2):
    def is_lower_set(self, fp: I.FinitePoset[X], s: List[X]) -> bool:
        raise NotImplementedError()

    def is_upper_set(self, fp: I.FinitePoset[X], s: List[X]) -> bool:
        raise NotImplementedError()


class SolFinitePosetClosures(I.FinitePosetClosures):
    def upper_closure(self, fp: I.FinitePoset[X], s: List[X]) -> List[X]:
        raise NotImplementedError()

    def lower_closure(self, fp: I.FinitePoset[X], s: List[X]) -> List[X]:
        raise NotImplementedError()


class SolFinitePosetInfSup(I.FinitePosetInfSup):
    def lower_bounds(self, fp: I.FinitePoset[E], s: List[E]) -> List[E]:
        raise NotImplementedError()

    def upper_bounds(self, fp: I.FinitePoset[E], s: List[E]) -> List[E]:
        raise NotImplementedError()

    def infimum(self, fp: I.FinitePoset[E], s: List[E]) -> Optional[E]:
        raise NotImplementedError()

    def supremum(self, fp: I.FinitePoset[E], s: List[E]) -> Optional[E]:
        raise NotImplementedError()


class SolFinitePosetMinMax(I.FinitePosetMinMax):
    def minimal(self, fp: I.FinitePoset[E], S: List[E]) -> List[E]:
        raise NotImplementedError()

    def maximal(self, fp: I.FinitePoset[E], S: List[E]) -> List[E]:
        raise NotImplementedError()
