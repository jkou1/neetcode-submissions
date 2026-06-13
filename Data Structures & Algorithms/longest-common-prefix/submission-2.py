class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""

        for j in range(len(strs[0])):
            i = 0
            cur_char = ''
            while i < len(strs):
                cur_char = strs[0][j]
                if j > len(strs[i])-1 or strs[i][j] != cur_char:
                    break
                i += 1

            if i == len(strs):
                longest_common_prefix += cur_char
            else:
                break
                    

        return longest_common_prefix