class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0 
        r = len(nums) - 1
        count = 0 
        while l<r:
            if target > nums[l] + nums[r]:
                count += r-l
                l+=1
            else:
                r-=1

        return count 






