# [0,  1, -1,  2, -1, -4]
# [0, -1,  1, -2,  1,  4]
 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        for i, i_num in enumerate(nums):
            complementary = i_num * (-1)
            seen = set()

            for j, j_num in enumerate(nums[i+1:]):

                part_of_complementary = complementary - j_num
                if part_of_complementary in seen:
                    result.add(tuple(sorted([i_num, j_num, part_of_complementary])))
                else:
                    seen.add(j_num)

        return [list(elem) for elem in result]