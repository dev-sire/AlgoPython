from ast import List
from collections import Counter

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        freq=Counter(p[1] for p in points)
        Sum, c2=0, 0
        for f in freq.values():
            if f<=1: continue
            c=f*(f-1)//2
            Sum+=c
            c2+=c*c
        return (Sum*Sum-c2)//2%(10**9+7)
        