class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            lookup = target - nums[i]
            if lookup in seen:
                l = [i,seen[lookup]]
            seen[nums[i]] = i
        return l


