class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Brute Force.. .. .. T.C = O(n^2)
        #                     S.C = O(1)
        # count = 0

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if target > nums[i] + nums[j]:
        #             count += 1
        # return count

        nums.sort()
        # [-1, 1, 1, 2, 3]
        l  = 0 ; r = len(nums) - 1 
        count = 0 
        while l<r:
            if target > nums[l] + nums[r]:
                count = count + (r-l)
                l+=1
            else:
                r-=1
        return count 

        