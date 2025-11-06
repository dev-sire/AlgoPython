import heapq
from collections import defaultdict

class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        parent = [i for i in range(c)]
        size = [1] * c
        mp = defaultdict(list)
        offline = [False] * c

        for i in range(c):
            heapq.heappush(mp[i], i)

        def findParent(node):
            if parent[node] != node:
                parent[node] = findParent(parent[node])
            return parent[node]

        def Union(u, v):
            up = findParent(u)
            vp = findParent(v)
            if up == vp:
                return
            if size[up] > size[vp]:
                size[up] += size[vp]
                parent[vp] = up
                while mp[vp]:
                    heapq.heappush(mp[up], heapq.heappop(mp[vp]))
            else:
                size[vp] += size[up]
                parent[up] = vp
                while mp[up]:
                    heapq.heappush(mp[vp], heapq.heappop(mp[up]))

        for u, v in connections:
            Union(u - 1, v - 1)

        ans = []

        for t, node in queries:
            node -= 1
            if t == 1:
                if not offline[node]:
                    ans.append(node + 1)
                    continue
                par = findParent(node)
                while mp[par] and offline[mp[par][0]]:
                    heapq.heappop(mp[par])
                ans.append(-1 if not mp[par] else mp[par][0] + 1)
            else:
                offline[node] = True

        return ans
