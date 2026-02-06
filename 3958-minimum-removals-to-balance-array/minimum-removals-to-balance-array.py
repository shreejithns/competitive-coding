class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()  # sort the array
        n = len(nums)  # get the length of the array
        max_window = 0  # to keep track of the largest valid window
        left = 0  # left pointer for the window
        for right in range(n):  # iterate with the right pointer
            while nums[right] > nums[left] * k:  # while the window is invalid
                left += 1  # move left pointer to the right
            max_window = max(max_window, right - left + 1)  # update max_window
        return n - max_window  # return the minimum removals