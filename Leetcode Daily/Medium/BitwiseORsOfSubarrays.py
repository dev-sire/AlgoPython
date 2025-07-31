class Solution:
    def subarrayBitwiseORs(self, arr):
        res = set()
        cur = set()
        for num in arr:
            cur = {num | x for x in cur} | {num}
            res |= cur
        return len(res)