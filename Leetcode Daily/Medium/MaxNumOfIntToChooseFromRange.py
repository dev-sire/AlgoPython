from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans = 0
        sum = 0
        bannedSet = set(banned)

        for i in range(1, n + 1):
            if i not in bannedSet and sum + i <= maxSum:
                ans += 1
                sum += i
        return ans