import sys
import typing as tp
from elementums import Elementum, Element

periodic = Elementum()

class ElemCombine():
    def __init__(self, cost: int, elm1: Element, elm2: Element) -> None:
        self.elm1 = elm1
        self.elm2 = elm2
        self.comb = set([elm1, elm2])
        self.cost = cost

    def __int__(self) -> int:
        return self.cost
    
    def __str__(self) -> str:
        return f"{self.cost:>2}   | {self.elm1.acronym:>2} + {self.elm2.acronym:>2}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.comb == other.comb
        else:
            another_class = other.__class__.__name__
            raise NotImplementedError(f'comparison between Element class and {another_class} is not supported')
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            another_class = other.__class__.__name__
            raise NotImplementedError(f'comparison between Element class and {another_class} is not supported')
        return self.cost < other.cost

    def __hash__(self) -> int:
        return hash(hash(self.elm1) + hash(self.elm2))


if len(sys.argv) != 2:
    exit(1)
target_num = int(sys.argv[1])
print(f"Target: {periodic.get4num(target_num).acronym}")
print("Cost | Elements")


useable_elementum: tp.List[Element] = []
with open("./useable_elementum20221015.txt") as f:
    for elm in f:
        acro = elm.strip()
        useable_elementum.append(periodic.get4acro(acro))

# print(useable_elementum)

res_list = []
for idx1, elm1 in enumerate(useable_elementum):
    for idx2, elm2 in enumerate(useable_elementum):
        if elm1.num + elm2.num == target_num:
            # print(f"{elm1.acronym:>2} + {elm2.acronym:>2} {idx1+idx2:>2}")
            res_list.append(ElemCombine(idx1+idx2, elm1, elm2))

res_list = list(set(res_list))
res_list.sort(key=lambda x:x.cost)
for item in res_list:
    print(item)
