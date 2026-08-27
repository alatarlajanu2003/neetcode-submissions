# abcad
# abcb

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        seen = set()

        while left < len(s):
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                right += 1

            longest = max(longest, right - left)

            if right >= len(s):
                break

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

        return longest


            