class Solution:
    def runningSum(self, nums):
        sum = 0
        arr = []
        for i in range(len(nums)):
            sum+=nums[i]
            arr.append(sum)
        return arr
