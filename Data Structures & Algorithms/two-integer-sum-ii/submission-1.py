# [1,2,3,4], target = 3
# start starts from 0, end starts from the end
# if sum > 3 then end -=1, if sum < 3 start += 1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            current_sum = numbers[start] + numbers[end]

            if current_sum == target:
                return [start + 1, end + 1]
            elif current_sum > target:
                end -= 1
            else:
                start += 1

        return []

