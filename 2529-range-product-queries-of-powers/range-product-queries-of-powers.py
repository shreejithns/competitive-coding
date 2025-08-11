class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        return (lambda a,MOD: [pow(2, a[r+1]-a[l], MOD) for l,r in queries])([0]+list(accumulate([i for i in range(31) if n>>i&1])), 10**9+7)