import math
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        INF = math.inf

        adj = [[] for _ in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])

        def dfs(node, visited, pathVisit, freq):
            if pathVisit[node]:
                return INF
            if visited[node]:
                return freq[node][26]
            
            visited[node] = 1
            pathVisit[node] = 1

            for nei in adj[node]:
                val = dfs(nei, visited, pathVisit, freq)
                if(val==INF): return INF
                for i in range(0, 26):
                    freq[node][i] = max(freq[node][i], freq[nei][i])
            
            freq[node][ord(colors[node])-ord('a')]+=1
            maxi = max(freq[node])
            pathVisit[node] = 0
            freq[node][26] = maxi
            return maxi
        
        freq=[[0 for _ in range(27)] for _ in range(n)]
        visited=[0] * n
        pathVisit = [0]*n

        ans = 0
        for node in range(n):
            if(not visited[node]):
                ans = max(ans, dfs(node, visited, pathVisit, freq))
                if(ans==INF): return -1

        return ans