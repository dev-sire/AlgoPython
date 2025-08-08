from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        N = 1
        while N <= n:
            N <<= 1
        
        segTree = [0] * (2 * N)
        
        for i in range(n):
            segTree[N + i] = baskets[i]
        
        for i in range(N - 1, 0, -1):
            segTree[i] = max(segTree[2 * i], segTree[2 * i + 1])
        
        count = 0
        for fruit in fruits:
            index = 1
            if segTree[index] < fruit:
                count += 1
                continue
            
            while index < N:
                if segTree[2 * index] >= fruit:
                    index = 2 * index
                else:
                    index = 2 * index + 1
            
            segTree[index] = -1
            while index > 1:
                index //= 2
                segTree[index] = max(segTree[2 * index], segTree[2 * index + 1])
        
        return count