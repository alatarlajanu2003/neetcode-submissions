# [1, 2, 3, 4, 5, 6, 7]
# 

class Solution:
    def is_target_in_arr(self, arr, target):
        start, end = 0, len(arr) - 1

        while start <= end:
            med = end - start // 2
            print(med)

            if arr[med] == target:
                return True
            elif arr[med] < target:
                start = med + 1
            else:
                end = med - 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if self.is_target_in_arr(matrix[i], target):
                return True
        
        return False



        # sol 1 (O(N^2))
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == target:
        #             return True

        # return False