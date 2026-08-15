# [-1,0,1,2,-1,-4]
# [-4, -1, -1, 0, 1, 2]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)
        seen_triplets = set()

        for i, num in enumerate(sorted_nums):

            complement = num * (-1)
            left, right = i + 1, len(sorted_nums) - 1

            while left < right:
                current_sum = sorted_nums[left] + sorted_nums[right]
                if current_sum == complement:
                    if (num, sorted_nums[left], sorted_nums[right]) not in seen_triplets:
                        result.append([num, sorted_nums[left], sorted_nums[right]])
                        seen_triplets.add((num, sorted_nums[left], sorted_nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < complement:
                    left += 1
                else:
                    right -= 1

        return result