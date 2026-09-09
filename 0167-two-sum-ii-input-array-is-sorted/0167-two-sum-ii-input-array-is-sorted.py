class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 ; r = len(numbers) - 1
        res = []
        
        while l<r:
            sum = numbers[l] + numbers[r]
            if target == sum:
                res.append(l+1)
                res.append(r+1)
                return res 
            elif target < sum:
                r-=1
            elif target > sum:
                l+=1


