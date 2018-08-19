import numpy as np


class Solution():
    
    def search(self, matrix, target):
        row, col = np.asarray(matrix).shape
        row_min, row_max, col_min, col_max = 0, row - 1, 0, col - 1
        
        # 缩小右侧列范围
        for j in range(col - 1, -1, -1):
            if matrix[0][j] > target:
                col_max = j - 1
        # 缩小左侧列范围
        for j in range(0, col_max + 1):
            if matrix[-1][j] < target:
                col_min = j + 1
        # 缩小上方行范围
        for i in range(0, row, 1):
            if matrix[i][col_max] < target:
                row_min = i + 1
        # 缩小下方行范围
        for i in range(row_max, row_min - 1, -1):
            if matrix[i][0] > target:
                row_max = i - 1
        # 小矩形内搜索
        for i in range(row_min, row_max + 1):
            for j in range(col_min, col_max + 1):
                if matrix[i][j] == target:
                    return i, j


s = Solution()
matrix = [
    [1, 2, 8, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],
    [6, 10, 11, 15],
]
target = 7
result = s.search(matrix, target)
print(result)
