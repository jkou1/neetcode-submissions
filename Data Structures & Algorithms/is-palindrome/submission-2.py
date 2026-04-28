class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        sAlNum = ""
        for char in s:
            if char.isalnum():
                sAlNum += char.lower()

        return (sAlNum[::-1] == sAlNum)