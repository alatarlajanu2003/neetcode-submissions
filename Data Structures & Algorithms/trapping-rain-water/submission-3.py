# min(hight(left), hight(right)) * (right - left - 1) - height(k)

# [0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
# [0, 1, 2, 3, 3, 3, 3, 3, 3, 3]

class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]
        right = [0]
        result = 0

        for i in range(1, len(height)):
            if height[i - 1] > left[i - 1]:
                left.append(height[i - 1])
            else:
                left.append(left[i - 1])

        height_reversed = list(reversed(height))

        for i in range(1, len(height_reversed)):
            if height_reversed[i - 1] > right[i - 1]:
                right.append(height_reversed[i - 1])
            else:
                right.append(right[i - 1])

        right_reversed = list(reversed(right))

        for i in range(len(left)):
            temp = min(left[i], right_reversed[i]) - height[i]
            result += temp if temp >= 0 else 0

        return result