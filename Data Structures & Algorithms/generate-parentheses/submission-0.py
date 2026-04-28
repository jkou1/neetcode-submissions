class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we can add opening parens whenever
        # closing parens? not so much. 
        # pop stuff off the stack when we can close it
        # every time we've found a string, add it to list
        # how to get all the combinations though?

        # we can alternate between adding an opening brace, 
        # or trying to close one
        # once we've added n opening braces, can't add anymore,
        # can only close
        # add opening:
        res = []
        curString = ""
        numOpen, numClose = 0, 0
        # maybe do a dfs search here? for all the different combos
        def recurse(curStr, no, nc):
            if no == nc and no == n:
                res.append(curStr)
                return
            # add an opening
            if no < n:
                curStr += "("
                recurse(curStr, no + 1, nc)
                curStr = curStr[:-1]
            
            if nc < no:
                curStr += ")"
                recurse(curStr, no, nc + 1)
        
        recurse(curString, numOpen, numClose)

        return res
