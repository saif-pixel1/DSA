class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum = 0 
        for i in range(len(nums)):
            rsum += nums[i]
        # 1 7 3 6 5 6
        # 0
        lsum = 0 
        for i in range(len(nums)):
            if lsum==rsum-nums[i]:
                return i
            else:
                lsum += nums[i]
                rsum -= nums[i]
        return -1
        