from ast import List
from collections import deque

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjacency list for the graph
        self.adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            # Convert to zero-based index
            self.adj[v1 - 1].append(v2 - 1)
            self.adj[v2 - 1].append(v1 - 1)

        # List to hold all connected components
        self.components = []
        self.fill_components(n)

        # Total count for all components
        total_ans = 0
        for comp in self.components:
            # Answer for the current component
            comp_ans = 0
            # Check if the component is bipartite
            if self.bipartite_check(comp[0], comp):
                for i in range(len(comp)):
                    comp_ans = max(comp_ans, self.bfs(comp[i], n))
                total_ans += comp_ans
            else:
                # Return -1 if the component is not bipartite
                return -1
        # Return the total count for all components
        return total_ans

    def fill_components(self, n: int):
        # Initialize visited list to track visited nodes
        visited = [False] * n
        def bfs(start):
            # Perform BFS to find all nodes in the connected component
            tmp = []
            visited[start] = True
            q = deque()
            q.append(start)
            while q:
                # Current node
                c = q.popleft()
                # Add to temporary component list
                tmp.append(c)
                # Check neighbors
                for val in self.adj[c]:
                    # If not visited
                    if not visited[val]:
                        visited[val] = True
                        q.append(val)
            # Return the found component
            return tmp

        # Iterate through all nodes to find all components
        for i in range(n):
            # If the node hasn't been visited
            if not visited[i]:
                # Perform BFS to fill the component
                x = bfs(i)
                # Add component to the list
                self.components.append(x)

    def bipartite_check(self, start: int, comp: List[int]) -> bool:
        # Check if the current component can be colored bipartitely
        # Initialize colors for the component
        color = {node: -1 for node in comp}
        q = deque([start])

        # Start coloring with 0
        color[start] = 0
        while q:
            # Current node
            node = q.popleft()
            for neigh in self.adj[node]:
                # Only process neighbors that belong to the current component
                if neigh not in color:
                    # Ignore nodes outside the component
                    continue
                # If uncolored
                if color[neigh] == -1:
                    # Color with opposite color
                    color[neigh] = 1 - color[node]
                    q.append(neigh)
                # If the same color, not bipartite
                elif color[neigh] == color[node]:
                    # Return False for non-bipartite
                    return False
        # Return True if bipartite
        return True

    def bfs(self, start: int, n: int) -> int:
        # BFS to count the number of nodes in the component
        tmp_comp_ans = 0
        # Reset visited for this BFS
        visited = [False] * n
        # Start from the current node
        q = deque([start])
        visited[start] = True
        
        while q:
            # Count the current node
            tmp_comp_ans += 1
            for _ in range(len(q)):
                # Current node to process
                curr = q.popleft()
                for neigh in self.adj[curr]:
                    # If neighbor is not visited
                    if not visited[neigh]:
                        # Add neighbor to queue
                        q.append(neigh)
                        # Mark as visited
                        visited[neigh] = True
        # Return the count for this BFS
        return tmp_comp_ans