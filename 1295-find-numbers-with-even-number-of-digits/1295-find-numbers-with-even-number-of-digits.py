class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0 
        for i in range(len(nums)):
            if 10<=nums[i]<=99:
                count+=1
            elif 1000<= nums[i]<=9999:
                count+=1
            elif nums[i] == 100000:
                count+=1
            else:
                continue
        return count


        
        