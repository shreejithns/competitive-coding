class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        #சூரியா அய்யா துணை | நிர்மல் ஸ்காரியா துணை 
        prefix = [0]*(len(nums))
        prefix[0] = nums[0]

        for i in range(1,len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
        
        count = 0
        for i in range(len(nums)-1): # comparing with last element
            if prefix[i] >= prefix[-1] - prefix[i]:
                count += 1

        return count

        