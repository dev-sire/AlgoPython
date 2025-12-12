from collections import Counter
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n, MOD=len(nums), 10**9+7
        freq, prev=Counter(nums), Counter()
        cnt=0
        prev[nums[0]]+=1
        for i in range(1, n-1):
            x=nums[i]
            x2=x<<1
            cnt+=prev[x2]*(freq[x2]-prev[x2]-(x==0))
            prev[x]+=1
        return cnt%MOD