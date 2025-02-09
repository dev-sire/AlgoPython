from ast import List

class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))
        self.Size = [1]*N

    def Find(self, x):
        if self.root[x] != x:
            self.root[x] = self.Find(self.root[x])  # path compression
        return self.root[x]

    def Union(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if x==y: return False

        if self.Size[x] > self.Size[y]:
            self.Size[x] += self.Size[y]
            self.root[y]=x
        else:
            self.Size[y] += self.Size[x]
            self.root[x]=y
        return True

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        N=n*n
        d=(0, 1, 0, -1, 0)
    
        def inside(i, j):
            return 0<=i<n and 0<=j<n
        def idx(i, j):
            return i*n+j

        G=UnionFind(N)
        maxSz=1
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x==1:
                    a=idx(i, j)
                    D=grid[i+1][j] if i<n-1 else 0
                    R=grid[i][j+1] if j<n-1 else 0
                    if D>0:
                        b=a+n
                        if G.Union(a, b):
                            maxSz=max(maxSz, G.Size[G.Find(a)])
                    if R>0:
                        b=a+1
                        if G.Union(a, b):
                            maxSz=max(maxSz, G.Size[G.Find(a)])
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x==0:
                    component=set()
                    for a in range(4):
                        r, s=i+d[a], j+d[a+1]
                        if inside(r, s) and grid[r][s]==1:
                            component.add(G.Find(idx(r, s)))
                    if len(component)==0: continue
                    sz=1+sum(G.Size[c] for c in component)
                    maxSz=max(maxSz, sz)
        return maxSz