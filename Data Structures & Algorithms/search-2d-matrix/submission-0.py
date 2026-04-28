class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # determine middle index in the matrix, then compare that value to target
        if not matrix or not matrix[0]:
            return False
        bottom, top = 0, len(matrix)-1
        mid = len(matrix) //2 
        while bottom <= top:
            mid = (bottom + top) // 2
            if target < matrix[mid][0]:
                top = mid - 1
            elif target > matrix[mid][-1]:
                bottom = mid + 1
            else:
                break
        if bottom > top:
            return False

        l, r = 0, len(matrix[0])-1
        
        while l <= r:
            m = (l + r) // 2
            if target < matrix[mid][m]:
                r = m - 1
            elif target > matrix[mid][m]:
                l = m + 1
            elif target == matrix[mid][m]:
                return True

        return False