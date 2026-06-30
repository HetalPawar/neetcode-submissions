class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        # increment col if target is greater than the row.
        # binary search twice, once vertical/columns then once rows
        up, down = 0, len(matrix)-1 # no of columns
        while up < down:
            mid = (up+down)//2
            if  target < matrix[mid][0] :
                down = mid - 1
            elif target > matrix[mid][-1] :
                up = mid+1
            else:
                break

        if not (up <= down):
            return False
        
        row = (up+down)//2 #the row in which target exists

        #now down is the row in which target is there
        left, right = 0, len(matrix[0])-1
        while left <= right:
            mid = (left + right)//2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid -1
            else:
                left = mid+1
            
        return False
        