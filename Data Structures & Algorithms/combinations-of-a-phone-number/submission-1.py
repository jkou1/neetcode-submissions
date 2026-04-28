class Solution:
    numToChar  = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        resList = []

        def backTrack(curString, i):
            if i == len(digits):
                resList.append(curString)
                return
            else:
                for ch in Solution.numToChar[digits[i]]:
                    backTrack(curString + ch, i + 1)   

        backTrack("", 0)

        return resList
            
