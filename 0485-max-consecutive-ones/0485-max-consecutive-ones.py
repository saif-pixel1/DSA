class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                l+=1
                if max < l:
                    max = l
            else:
                l = 0 
        return max
                
        