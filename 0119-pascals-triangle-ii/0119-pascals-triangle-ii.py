class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def nCr(n,r):
            res = 1
            for i in range(r):
                res = res * (n-i)
                res = res // (i+1)
            return res 
        
        l = []
        for i in range(rowIndex+1):
            l.append(nCr(rowIndex,i))
        return l

        