class Solution:
    def minimumCost(self, a: List[int]) -> int:
        return a[0]+sum(nsmallest(2,islice(a,1,None)))