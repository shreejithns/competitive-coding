class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        Find maximum sum of subarrays where each subarray has exactly k elements
        and subarrays don't overlap
        
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)           # total number of elements
        a = [0] * n             # stores max sum ending at each position
        s = sum(nums[:k])       # sum of first k-sized subarray
        a[k-1] = s              # store first subarray sum
        r = s                   # track overall maximum
        
        # 🔄 SLIDE WINDOW: Process remaining positions
        for i in range(k, n):
            # Update sliding window sum
            s += nums[i] - nums[i-k]
            
            # 💡 KEY DECISION: Take current subarray alone OR combine with previous
            a[i] = s + (0 if 0 > a[i-k] else a[i-k])
            
            # 📊 UPDATE MAXIMUM: Track best result
            r = a[i] if a[i] > r else r
        
        return r