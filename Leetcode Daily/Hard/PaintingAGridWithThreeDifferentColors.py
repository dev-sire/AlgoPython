from functools import cache

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        @cache
        def g(prev):
            def gg(i,cur):
                if i==m: return [cur]
                return sum((gg(i+1,cur+cand) for cand in 'rgb'
                    if prev[i]!=cand and (i==0 or cur[-1]!=cand)),[])

            return gg(0,'')

        @cache
        def f(j,prev):
            if j==n: return 1
            return sum(f(j+1,cur) for cur in g(prev))%(10**9+7)

        return f(0,'_'*m)