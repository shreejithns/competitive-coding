class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        N = len(prices)
        curr = [[-inf] * 3 for _ in range(N+1)]
        prev = [[0, -inf, -inf] for _ in range(N+1)]
        curr[N][0] = 0

        for w in range(1, k+1):
            for i in range(N-1, -1, -1):
                curr[i][1] = max(prev[i+1][0] - prices[i], curr[i+1][1])
                curr[i][2] = max(prev[i+1][0] + prices[i], curr[i+1][2])
                curr[i][0] = max(curr[i+1][1] + prices[i], curr[i+1][2] - prices[i], curr[i+1][0])
            curr, prev = prev, curr
        return prev[0][0]