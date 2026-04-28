class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #  first just check the first items of each row with bin search

        t, b = 0, len(matrix)-1
        m = 0
        while t <= b:
            m = (t + b) // 2
            if target > matrix[m][-1]:
                t = m + 1
            elif target < matrix[m][0]:
                b = m - 1
            else:
                break
        
        
        # we need to to the same for each row, use bin search
        l, r = 0, len(matrix[0]) - 1
        m2 = 0
        while l <= r:
            m2 = (l + r) // 2
            if matrix[m][m2] < target:
                l = m2 + 1
            elif matrix[m][m2] > target:
                r = m2 - 1
            else:
                return True

        return False