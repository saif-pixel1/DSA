class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        k = 0 
        res = []
        while k<len(nums)-2:
            if k > 0 and nums[k] == nums[k-1]:
                k+=1
                continue
            l = k+1
            r = len(nums) - 1
            while l<r:
                sum = nums[l] + nums[k] + nums[r]
                if sum ==0:
                    res.append([nums[l], nums[k], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
 
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
    
                elif sum > 0:
                    r-=1
                else:
                    l+=1

            k+=1
        return res

        