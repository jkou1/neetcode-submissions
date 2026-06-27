from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = defaultdict(list)
        resList = []

        for s in strs:
            key = "".join(sorted(s))
            anagram_dict[key].append(s)

        
        for _, v in anagram_dict.items():
            resList.append(v)
        
        return resList