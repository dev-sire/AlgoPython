from math import isqrt

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i+1] = pref[i] + (ch == '1')

        Z = [i for i, ch in enumerate(s) if ch == '0']
        m = len(Z)

        ans = 0

        i = 0
        while i < n:
            if s[i] == '0':
                i += 1
                continue
            j = i
            while j < n and s[j] == '1':
                j += 1
            L = j - i
            ans += L * (L + 1) // 2
            i = j

        B = isqrt(n) + 2

        def ones(l, r):
            return pref[r+1] - pref[l]

        for a in range(m):
            Lmin = 0 if a == 0 else Z[a-1] + 1
            Lmax = Z[a]
            if Lmin > Lmax:
                continue

            for z in range(1, B + 1):
                b = a + z - 1
                if b >= m:
                    break

                Rmin = Z[b]
                Rmax = Z[b + 1] - 1 if b + 1 < m else n - 1
                if Rmin > Rmax:
                    continue

                need = z * z
                r = Rmin

                for l in range(Lmin, Lmax + 1):
                    if pref[Rmax + 1] - pref[l] < need:
                        continue
                    while r <= Rmax and ones(l, r) < need:
                        r += 1
                    if r > Rmax:
                        break
                    ans += (Rmax - r + 1)

        return ans