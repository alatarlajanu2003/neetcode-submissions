# [2,20,4,10,3,4,1,5] -> 1, 10, 20

# {2,20,4,10,3,4,1,5}
# 2: is 1 in set => yes
# 20: is 19 in set => no => is 21 in set => no => count = 1
# 10: ...
# 1 => is 2 in set => yes, local_c ++, is 3 in set 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_nums = set(nums)
        count = 1

        for num in unique_nums:
            if num - 1 in unique_nums:
                continue

            i = 1
            local_count = 1
            while num + i in unique_nums:
                local_count += 1
                i += 1

            count = max(count, local_count)

        return count

