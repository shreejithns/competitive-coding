class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        op0=0
        for i, c in enumerate(s):
            if (i&1)==(ord(c)&1):
                op0+=1
        return min(op0, n-op0)