class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # swap arrays if nums1 is larger
        
        m, n = len(nums1), len(nums2)  # lengths of the arrays
        left, right = 0, m  # binary search range on nums1
        
        while left <= right:  # binary search loop
            i = (left + right) // 2  # partition index for nums1
            j = (m + n + 1) // 2 - i  # partition index for nums2
            
            # Handle edge cases for partitioning
            maxLeftA = float('-inf') if i == 0 else nums1[i - 1]  # max of left part of nums1
            minRightA = float('inf') if i == m else nums1[i]  # min of right part of nums1
            maxLeftB = float('-inf') if j == 0 else nums2[j - 1]  # max of left part of nums2
            minRightB = float('inf') if j == n else nums2[j]  # min of right part of nums2
            
            # Check if correct partition is found
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                # If total length is odd, median is max of left parts
                if (m + n) % 2 == 1:
                    return max(maxLeftA, maxLeftB)  # return median for odd length
                # If even, median is average of max of left and min of right
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2.0  # return median for even length
            elif maxLeftA > minRightB:
                right = i - 1  # move left in nums1
            else:
                left = i + 1  # move right in nums1