class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainder_index_map = {0: -1}
        sum = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            if k != 0:
                sum %= k
            
            # Check if the remainder has been seen before
            if sum in remainder_index_map:
                if i - remainder_index_map[sum] > 1:  # If subarray length is greater than 1, return true
                    return True
            else:  # Store the index of the first occurrence of the remainder
                remainder_index_map[sum] = i
        
        # If no valid subarray is found, return False
        return False