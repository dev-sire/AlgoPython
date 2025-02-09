from ast import List
from itertools import pairwise

class Solution:
    def check(self, nums: List[int]) -> bool:
        return (cntD:=sum(y<x for x, y in pairwise(nums)))==0 or (cntD==1 and nums[-1]<=nums[0])