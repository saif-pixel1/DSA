class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l =0 
        r = len(nums) - 1
        res = [0] * len(nums)
        i = len(nums) - 1
        while l<=r:
            if nums[l]*nums[l] < nums[r]*nums[r]:
                # res.append(nums[r]**2)
                res[i] = nums[r]*nums[r]
                r-=1
            else:
                # res.append(nums[l]**2)
                res[i] = nums[l]*nums[l]
                l+=1
            i-=1
        return res 
        
        