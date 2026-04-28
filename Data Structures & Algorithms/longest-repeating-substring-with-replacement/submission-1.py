class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        from collections import defaultdict

        charCounts = defaultdict(int)
        maxLen = 0
        mostCommon = 0
        l, r = 0, 0

        for i in range(len(s)):
            charCounts[s[i]] += 1
            
            mostCommon = max(mostCommon, charCounts[s[i]])
            # if window size minus mostCommon elt is more 
            # than what we can replace, need to shift l over by 1

            if (r - l + 1) - mostCommon > k:
                charCounts[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
            r += 1


        return maxLen