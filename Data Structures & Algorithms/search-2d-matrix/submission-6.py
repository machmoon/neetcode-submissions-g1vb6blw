class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix[0]) * len(matrix) - 1

        while l <= r:

            mid = (l+r)//2
            middle_row_index = mid // len(matrix[0]) 
            middle_col_index = mid % len(matrix[0]) 

            print(middle_row_index,middle_col_index)
            value = matrix[middle_row_index][middle_col_index]

            if value < target:
                l = mid + 1
            elif value > target:
                r = mid - 1
            else:
                return True
        return False
