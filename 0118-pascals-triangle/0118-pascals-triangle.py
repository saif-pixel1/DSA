class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[1]]
        prev = [1]
        for i in range(1, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(prev[j] + prev[j-1])
            temp.append(1)
            prev = temp
            l.append(prev)
        return l

        