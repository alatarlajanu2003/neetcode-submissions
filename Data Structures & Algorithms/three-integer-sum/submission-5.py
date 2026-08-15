# -2,0,0,2,2
# -2, 0, 0, 2, 2

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)
        i = 0

        while i < len(sorted_nums):
            if i > 0 and (sorted_nums[i] == sorted_nums[i-1]):
                i += 1
                continue              

            complement = sorted_nums[i] * (-1)
            left, right = i + 1, len(sorted_nums) - 1

            while left < right:
                current_sum = sorted_nums[left] + sorted_nums[right]
                if current_sum == complement:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    while left < right and sorted_nums[left] == sorted_nums[left-1]:
                        left += 1
                    right -= 1
                elif current_sum < complement:
                    left += 1
                else:
                    right -= 1
            
            i += 1

        return result