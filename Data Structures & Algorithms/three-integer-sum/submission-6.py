# -2,0,0,2,2
# -2, 0, 0, 2, 2

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        i = 0

        while i < len(nums):
            if i > 0 and (nums[i] == nums[i-1]):
                i += 1
                continue              

            complement = nums[i] * (-1)
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == complement:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    right -= 1
                elif current_sum < complement:
                    left += 1
                else:
                    right -= 1
            
            i += 1

        return result