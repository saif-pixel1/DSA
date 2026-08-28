class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
    # TC = O(n) ; SC = O(1)
        sum = 0
        max = 0 
        for i in range(len(gain)):
            sum += gain[i]
            if max < sum:
                max =sum
        return max 


        