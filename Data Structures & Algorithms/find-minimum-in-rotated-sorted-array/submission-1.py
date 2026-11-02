# 1 2 3 4 5, if left < mid and left < right => right = mid - 1
# 5 1 2 3 4, l = 0, m = 2, r = 4; if left > mid and left > right => right = mid - 1
# 3 4 5 1 2, left < mid and left > right => left = mid + 1

# 4 5 1 2 3 => l (mid < right)

# 3 4 5 1 2 => r (mid > right)
# 2 3 4 5 1 => r

# 5 1 2 3 4 => l (mid < right)
# 1 2 3 4 5 => l 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
        