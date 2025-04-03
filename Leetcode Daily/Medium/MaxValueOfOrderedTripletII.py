from ast import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        maxDiff = 0
        maxNum = 0

        for num in nums:
            ans = max(ans, maxDiff * num)
            maxDiff = max(maxDiff, maxNum - num)
            maxNum = max(maxNum, num)

        return ans