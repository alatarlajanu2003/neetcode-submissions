# [1, 2, 3, 4, 5] => [1, 2, 3, 4, 5]
# [4, 5, 1, 2, 3] => [4, 5], [1, 2, 3], l = 2
# [2, 3, 4, 5, 1]

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        # l if basically the index after which everything is sorted and before each as well
        def search_temp(left, right):
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return - 1

        found_in_first_arr = search_temp(0, max(0, l - 1))
        found_in_second_arr = search_temp(l, len(nums) - 1)

        return found_in_first_arr if found_in_first_arr != -1 else found_in_second_arr



