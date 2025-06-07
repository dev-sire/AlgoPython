from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
#-----------------------------------------------------------
        # Solution 2:
#-----------------------------------------------------------
        n = len(edges)
        dist1, d, curr = [-1] * n, 0, node1
        while curr != -1 and dist1[curr] == -1:
            dist1[curr] = d
            d += 1
            curr = edges[curr]

        best, res = float('inf'), -1
        seen, d, curr = [False] * n, 0,  node2
        while curr != -1 and not seen[curr]:
            seen[curr] = True
            if dist1[curr] != -1:
                m = max(dist1[curr], d)
                if m < best or (m == best and curr < res):
                    best, res = m, curr
            d += 1
            curr = edges[curr]

        return res