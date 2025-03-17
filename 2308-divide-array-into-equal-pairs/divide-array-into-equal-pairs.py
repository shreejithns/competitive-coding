class Solution(object):
    def divideArray(self, nums):
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        return all(count % 2 == 0 for count in frequency.values())

            