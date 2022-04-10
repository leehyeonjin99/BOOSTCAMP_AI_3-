class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        ''' Runtime 259ms
        for i in range(m):
            if target in matrix[i]:
                print("result",matrix[i])
                return True
        return False       
        '''
        #180ms
        for i in range(m):
            left, right = 0, n-1
            while left <= right:
                mid = (left+right)//2
                if target == matrix[i][mid]:
                    return True
                elif target < matrix[i][mid]:
                    right = mid-1
                else:
                    left = mid+1
        return False
