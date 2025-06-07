class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Step 1: Initialize parent array
        parent = list(range(26))  # 'a' to 'z' represented as 0 to 25

        # Step 2: Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Step 3: Union with lexicographical priority
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        # Step 4: Build equivalence groups
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        # Step 5: Transform baseStr
        result = []
        for ch in baseStr:
            smallest = chr(find(ord(ch) - ord('a')) + ord('a'))
            result.append(smallest)

        return ''.join(result)