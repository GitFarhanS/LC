class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1
        while left <= right:
            middle = (right+left)//2
            x, y = divmod(middle, len(matrix[0]))
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                left = middle + 1
            else:
                right = middle -1
        return False
