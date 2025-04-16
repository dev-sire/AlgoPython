from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        
        freq = defaultdict(int)
        prev_count = 0
        res = 0
        left = 0
        
        for right in range(len(nums)):
            prev_count += freq[nums[right]]
            freq[nums[right]] += 1
            
            while prev_count >= k:
                res += len(nums) - right
                prev_count -= freq[nums[left]] - 1
                freq[nums[left]] -= 1
                left += 1
        
        return res