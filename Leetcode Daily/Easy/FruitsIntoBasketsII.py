from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        alloted = 0

        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    alloted += 1
                    baskets[j] = -1  
                    break

        return n - alloted