from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        odd = 0
        even = 0
        for i in arr:
            even += 1
            if i % 2:
                odd, even = even, odd
            res = (res + odd) % ((10**9) + 7)
        return res       