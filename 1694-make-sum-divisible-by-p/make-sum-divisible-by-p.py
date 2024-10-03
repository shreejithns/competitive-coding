class Solution:
    def minSubarray(self, nums, p):
        totalSum = sum(nums)
        remainder = totalSum % p

        if remainder == 0:
            return 0

        n = len(nums)
        minLength = n
        prefixSum = 0
        prefixSums = {0: -1}

        for i in range(n):
            prefixSum = (prefixSum + nums[i]) % p
            target = (prefixSum - remainder + p) % p

            if target in prefixSums:
                minLength = min(minLength, i - prefixSums[target])

            prefixSums[prefixSum] = i

        return minLength if minLength < n else -1