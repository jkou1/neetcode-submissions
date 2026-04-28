class Solution:
    def isPalindrome(self, s: str) -> bool:
        hi = len(s)-1
        s2 = ""
        s1 = ""
        if len(s) == 1:
            return True
        else:
            s = s.lower()
            while hi > -1:
                if s[hi].isalnum():
                    s2 = s2 + s[hi]
                    s1 = s[hi] + s1
                hi -= 1
            return s1 == s2
        