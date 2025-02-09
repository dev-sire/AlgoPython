from ast import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = []
        visited = set()
        memo = [0] * n

        def dfs(i):
            if memo[i] == 1 or len(graph[i]) == 0:
                return True
            elif memo[i] == -1 or i in visited:
                return False
            
            visited.add(i)
            
            for neighbour in graph[i]:
                if not dfs(neighbour):
                    memo[i] = -1
                    return False

            memo[i] = 1
            return True
        
        for i in range(n):
            if dfs(i):
                res.append(i)
        
        return res