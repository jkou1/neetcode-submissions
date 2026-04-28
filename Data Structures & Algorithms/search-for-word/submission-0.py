class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # check cur elt, then check corners
        # but wait, what if we go up, then our up neighbor checks below?
        # this isn't allowed, so we need to mark cur board tile
        # as a non-alpha char
        
        def helper(i, j, ind):
            if ind == len(word):
                return True
            if i >= len(board) or i < 0 or j < 0 or j >= len(board[0]) or board[i][j] != word[ind]:
                return False
            
            

            # here, we check cur spot, and our up, down, l r if they're in bounds
            # can generalize this if statement to all indicies of the word
            # how? just pass the proper index into func
            
            # we mark cur spot as an invalid char, let's use *
            temp = board[i][j]
            board[i][j] = "*"
            # call func on neighbors? how do we know that we can?
            foundTF = (helper(i + 1, j, ind + 1) or helper(i, j + 1, ind + 1) or 
            helper(i - 1, j, ind + 1) or helper(i, j - 1, ind + 1))
            # reset what cur board slot contains
            board[i][j] = temp
            return foundTF
        
        # now need to start calling at each tile, bc each tile could be a valid start
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, 0):

                    return True

        return False




