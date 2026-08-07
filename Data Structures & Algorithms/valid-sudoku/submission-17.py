# 1: 00
# 2: 01
# 3: 04
# 4: 10
# 5: 13
# 9: 21

# 00 01; 00 02; 00 03
# 01; 02; 03

# 00 10; 00 11; 00 12
# 10; 11, 12

# 00 20; 00 21; 00 22
# 20; 21; 22

# for the same num:

# |x1 - x2| > 3 || |y1 - y2| > 3
# if holds -> update latest position
# if not -> return false

# if x1 == x2 or y1 == y2 -> return false

# return true in the end

# how to identify if they are in the same square?

from collections import defaultdict

class Solution:
    def create_small_square_indentifier_matrix(self, matrix: List[List[str]]) -> List[List[str]]:
        return [
            [0,0,0,1,1,1,2,2,2],
            [0,0,0,1,1,1,2,2,2],
            [0,0,0,1,1,1,2,2,2],
            [3,3,3,4,4,4,5,5,5],
            [3,3,3,4,4,4,5,5,5],
            [3,3,3,4,4,4,5,5,5],
            [6,6,6,7,7,7,8,8,8],
            [6,6,6,7,7,7,8,8,8],
            [6,6,6,7,7,7,8,8,8]
        ]


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_latest_position = defaultdict(str)
        matrix_with_square_indicators = self.create_small_square_indentifier_matrix(board)

        for row_index in range(len(board)):
            for column_index in range(len(board[row_index])):
                
                num = board[row_index][column_index]
                if not num.isnumeric():
                    continue

                latest_position_of_num = num_latest_position[num]

                if not latest_position_of_num:
                    num_latest_position[num] = f"{row_index}{column_index}"
                else:
                    x_pos = int(latest_position_of_num[0])
                    y_pos = int(latest_position_of_num[1])

                    # row
                    if row_index == x_pos:
                        return False

                    # column
                    if column_index == y_pos:
                        return False

                    # 3 x 3
                    if abs(row_index - x_pos) <= 2 and abs(column_index - y_pos) <= 2 and matrix_with_square_indicators[row_index][column_index] == matrix_with_square_indicators[x_pos][y_pos]:
                        return False

                    num_latest_position[num] = f"{row_index}{column_index}"

        return True










