from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        INF = 10**30
        minPrefix = [INF] * k
        minPrefix[0] = 0

        prefix = 0
        answer = -10**30

        for i, x in enumerate(nums):
            prefix += x
            mod = (i + 1) % k

            if minPrefix[mod] != INF:
                answer = max(answer, prefix - minPrefix[mod])

            minPrefix[mod] = min(minPrefix[mod], prefix)

        return answer