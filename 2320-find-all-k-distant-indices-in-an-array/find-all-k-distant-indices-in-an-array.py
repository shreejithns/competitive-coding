class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        n = len(nums)
        diff = [0] * (n + 1)
        result = []

        for i in range(n):
            if nums[i] == key:
                start = max(0, i - k)
                end = min(n, i + k + 1)
                diff[start] += 1
                if end < n:
                    diff[end] -= 1

        s = 0
        for i in range(n):
            s += diff[i]
            if s > 0:
                result.append(i)

        return result