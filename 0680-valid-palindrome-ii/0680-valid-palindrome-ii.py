class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(l,r,s):
            while l<r:
                if s[l] !=s[r]:
                    return False
                l+=1
                r-=1
            return True

        l = 0
        r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                # a superpower 
                # abbxa
                # i 
                #     j
                return helper(l+1,r,s) or helper(l,r-1,s)
            l +=1
            r-=1
        return True
                










