class Solution:
    def sortedSquares(self, nums):
        squared_arr = [x**2 for x in nums]
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            P = arr[-1]
            L = [i for i in arr[:-1] if i <= P]
            R = [j for j in arr[:-1] if j > P]
            L = quick_sort(L)
            R = quick_sort(R)
            return L + [P] + R
        return quick_sort(squared_arr)


        
        

        