# [1, 2, 3, 4, 5, 6, 7]
# 

class Solution:
    # option 3 log(NM)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count = len(matrix)
        column_count = len(matrix[row_count - 1])

        start, end = 0, row_count * column_count - 1

        while start <= end:
            med = start + (end - start) // 2
            print(med)
            print(med // column_count, med % column_count)
            med_elem = matrix[med // column_count][med % column_count]

            if med_elem == target:
                return True
            elif med_elem < target:
                start = med + 1
            else:
                end = med - 1

        return False




    # option 2, NlogM
    # def is_target_in_arr(self, arr, target):
    #     start, end = 0, len(arr) - 1

    #     while start <= end:
    #         med = start + (end - start) // 2

    #         if arr[med] == target:
    #             return True
    #         elif arr[med] < target:
    #             start = med + 1
    #         else:
    #             end = med - 1
        
    #     return False

    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     for i in range(len(matrix)):
    #         if self.is_target_in_arr(matrix[i], target) and target >= matrix[i][0] and target <= matrix[i][len(matrix[i]) - 1]:
    #             return True
        
    #     return False

        # sol 1, NM
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == target:
        #             return True

        # return False